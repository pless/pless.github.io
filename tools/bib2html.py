#!/usr/bin/env python3
"""BibTeX to HTML for the publications page of pless.github.io.

render(bib_path) returns the publication list (a by-year view and a by-type
view) that tools/build.py puts between the publications markers.
Python 3 standard library only.

The order and the sections are those of the old PHP site (bibtexbrowser):
entries run newest year first and, inside a year, by BibTeX key in descending
order; the number [N] of an entry is its place counted from the oldest.
"""
import html
import re
import unicodedata
from dataclasses import dataclass
from itertools import groupby
from pathlib import Path

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
TAG_FIELDS = ("annote", "annotation", "annotations")


# ---------- reading BibTeX ----------

@dataclass
class Entry:
    kind: str
    key: str
    fields: dict   # lower-case field name -> expanded text; the last one wins
    tags: list
    raw: str       # the entry as written in the file


ENTRY_START = re.compile(r"@\s*([A-Za-z]+)\s*\{")
FIELD_NAME = re.compile(r"[\s,;]*([^\s\"#%'(),={}]+)\s*(=?)\s*")
BARE_TOKEN = re.compile(r"[^\s\"#%'(),={}]+")


def closing_brace(text, start):
    """Index of the } that matches the { at text[start]; len(text) if none does."""
    depth = 0
    for i in range(start, len(text)):
        if text[i] in "{}" and text[i - 1] != "\\":
            depth += 1 if text[i] == "{" else -1
            if depth == 0:
                return i
    return len(text)


def closing_quote(text, start):
    """Index of the " that ends the quoted string starting at text[start]."""
    depth = 0
    for i in range(start + 1, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
        elif text[i] == '"' and depth == 0:
            return i
    return len(text)


def parse_piece(text, i, macros):
    """One piece of a value: {braced}, "quoted", a number or a macro name."""
    while text[i:i + 1].isspace():
        i += 1
    if text[i:i + 1] == "{":
        end = closing_brace(text, i)
        return text[i + 1:end], end + 1
    if text[i:i + 1] == '"':
        end = closing_quote(text, i)
        return text[i + 1:end], end + 1
    match = BARE_TOKEN.match(text, i)
    if not match:
        return "", i
    token = match.group()
    return (token if token.isdigit() else macros.get(token.lower(), token)), match.end()


def parse_value(text, i, macros):
    """A value with its pieces joined by #. Returns (text, next index)."""
    parts = []
    while True:
        piece, i = parse_piece(text, i, macros)
        parts.append(piece)
        j = i
        while text[j:j + 1].isspace():
            j += 1
        if text[j:j + 1] != "#":
            return "".join(parts), i
        i = j + 1


def parse_fields(text, macros):
    """List of (lower-case name, value). Junk between fields is skipped."""
    pairs, i = [], 0
    while True:
        match = FIELD_NAME.match(text, i)
        if not match:
            return pairs
        i = match.end()
        if match.group(2) or text[i:i + 1] in ('{', '"'):   # "name{...}" misses its =
            value, i = parse_value(text, i, macros)
            pairs.append((match.group(1).lower(), value))


def split_entries(text):
    """Yield (kind, body, raw text) for every @entry; the rest is junk."""
    pos = 0
    while True:
        match = ENTRY_START.search(text, pos)
        if not match:
            return
        line_start = text.rfind("\n", 0, match.start()) + 1
        if text[line_start:match.start()].lstrip().startswith("%"):
            pos = match.end()
            continue
        end = closing_brace(text, match.end() - 1)
        if end == len(text):
            line = text.count("\n", 0, match.start()) + 1
            raise ValueError("bib entry at line %d is never closed" % line)
        yield match.group(1).lower(), text[match.end():end], text[match.start():end + 1]
        pos = end + 1


def tags_of(pairs):
    tags = []
    for name, value in pairs:
        if name in TAG_FIELDS:
            for tag in re.split(r"[,\s]+", clean(value).lower()):
                if tag and tag not in tags:
                    tags.append(tag)
    return tags


def parse_bib(text):
    macros = {name[:3].lower(): name for name in MONTHS}
    entries = []
    for kind, body, raw in split_entries(text):
        if kind == "string":
            for name, value in parse_fields(body, macros):
                macros[name] = value
        elif kind not in ("comment", "preamble"):
            key, _, rest = body.partition(",")
            pairs = parse_fields(rest, macros)
            entries.append(Entry(kind, key.strip(), dict(pairs), tags_of(pairs), raw))
    return entries


# ---------- LaTeX and encoding to plain Unicode ----------

ACCENTS = {'"': "\u0308", "'": "\u0301", "`": "\u0300", "^": "\u0302",
           "~": "\u0303", "=": "\u0304", ".": "\u0307", "c": "\u0327",
           "v": "\u030c", "H": "\u030b", "u": "\u0306", "r": "\u030a",
           "k": "\u0328"}
LETTERS = {"ss": "ß", "aa": "å", "AA": "Å", "ae": "æ", "AE": "Æ", "oe": "œ",
           "OE": "Œ", "o": "ø", "O": "Ø", "l": "ł", "L": "Ł", "i": "ı", "j": "ȷ"}
MATH = {"\\times": "×", "\\cdot": "·", "\\pm": "±"}

MOJIBAKE = re.compile("[\u00c2-\u00df][\u0080-\u00bf]|[\u00e0-\u00ef][\u0080-\u00bf]{2}"
                      "|[\u00f0-\u00f4][\u0080-\u00bf]{3}")
ZERO_WIDTH = re.compile("[\u200b\u200c\u200d\u2060\ufeff]")
MATH_SPAN = re.compile(r"(?<!\\)\$([^$]*)\$")
SYMBOL_ACCENT = re.compile(r"""\\(["'`^~=.])\s*(?:\{\s*(\\?[A-Za-z])\s*\}|(\\?[A-Za-z]))""")
WORD_ACCENT = re.compile(r"\\([cvHurk])(?:\s+(\\?[A-Za-z])|\s*\{\s*(\\?[A-Za-z])\s*\})")
SPECIAL_LETTER = re.compile(r"\\(ss|aa|AA|ae|AE|oe|OE|[oOlLij])(?![A-Za-z])(?:\{\}|\s+)?")


def fix_encoding(text):
    """Undo UTF-8 read as Latin-1 ("â\\x80\\x8b") and drop zero-width characters."""
    def undo(match):
        try:
            return match.group().encode("latin-1").decode("utf-8")
        except UnicodeError:
            return match.group()
    return ZERO_WIDTH.sub("", MOJIBAKE.sub(undo, text))


def accent(match):
    mark = ACCENTS[match.group(1)]
    letter = match.group(2) or match.group(3)
    return unicodedata.normalize("NFC", letter.lstrip("\\") + mark)


def math_to_text(match):
    inner = match.group(1)
    for command, char in MATH.items():
        inner = inner.replace(command, char)
    return inner


def latex_to_unicode(text):
    text = MATH_SPAN.sub(math_to_text, text)
    text = SYMBOL_ACCENT.sub(accent, text)
    text = WORD_ACCENT.sub(accent, text)
    text = SPECIAL_LETTER.sub(lambda m: LETTERS[m.group(1)], text)
    text = re.sub(r"\\([&%$#_])", r"\1", text)
    text = text.replace("---", "\u2014").replace("--", "\u2013")
    text = text.replace("``", "\u201c").replace("''", "\u201d")
    text = re.sub(r"\\~(\{\})?", "\x00", text).replace("~", " ").replace("\x00", "~")   # \~{} is a real ~
    text = re.sub(r"\\[A-Za-z]+\s*", "", text)   # \textit{x}, \emph{x}, ...: keep x
    return re.sub(r"[\\{}$]", "", text)


def clean(text):
    """Text of a BibTeX field as it is shown on the page."""
    text = latex_to_unicode(fix_encoding(text))
    return unicodedata.normalize("NFC", re.sub(r"\s+", " ", text).strip())


def clean_url(url):
    url = re.sub(r"\\([~&%#_$])(\{\})?", r"\1", fix_encoding(url))
    return re.sub(r"[\s{}]", "", url)


# ---------- names and the line of text after the title ----------

def split_names(value):
    """Split a BibTeX name list at 'and' (any case) outside braces."""
    parts, depth, start = [], 0, 0
    for match in re.finditer(r"[{}]|\s+and\s+", value, re.I):
        if match.group() == "{":
            depth += 1
        elif match.group() == "}":
            depth -= 1
        elif depth == 0:
            parts.append(value[start:match.start()])
            start = match.end()
    return parts + [value[start:]]


def display_names(value):
    """'Last, First and First Last and others' -> ['First Last', 'First Last', 'et al.']"""
    names = []
    for chunk in split_names(value):
        chunk = clean(chunk)
        parts = [part.strip() for part in chunk.split(",")]
        if chunk == "others":
            names.append("et al.")
        elif len(parts) == 2 and all(len(part.split()) > 1 for part in parts):
            names.extend(parts)               # "Ann Lee, Bob Roe": 'and' left out
        elif len(parts) == 2:
            names.append(parts[1] + " " + parts[0])
        elif chunk:
            names.append(chunk)
    return names


def year_of(entry):
    match = re.search(r"\d{4}", entry.fields.get("year", ""))
    return int(match.group()) if match else 0


def people_text(entry):
    """The names in parentheses after the title: authors, or else editors."""
    fields = entry.fields
    if fields.get("author"):
        return "(" + ", ".join(display_names(fields["author"])) + ")"
    if fields.get("editor"):
        return "(" + ", ".join(display_names(fields["editor"])) + ", eds.)"
    return ""


def venue_and_note(entry):
    """('In <booktitle or journal>', note). A patent's note is its venue."""
    fields = entry.fields
    where = clean(fields.get("booktitle") or fields.get("journal") or "")
    note, comment = clean(fields.get("note", "")), clean(fields.get("comment", ""))
    venue = ""
    if where:
        venue = "In " + where
        if fields.get("author") and fields.get("editor"):
            venue += " (" + ", ".join(display_names(fields["editor"])) + ", eds.)"
    elif entry.kind == "misc":
        venue, note = note, ""
    return venue, "; ".join(text for text in (note, comment) if text)


def publisher_text(entry):
    fields = entry.fields
    if entry.kind == "phdthesis":
        return ", ".join(text for text in ("PhD thesis", clean(fields.get("school", ""))) if text)
    return clean(fields.get("publisher", ""))


def citation_html(entry):
    """(authors), In venue, publisher, volume N, year. (note)"""
    venue, note = venue_and_note(entry)
    people = people_text(entry)
    volume = clean(entry.fields.get("volume", ""))
    parts = [
        '<span class="pub-authors">%s</span>' % esc(people) if people else "",
        '<span class="pub-venue">%s</span>' % esc(venue) if venue else "",
        esc(publisher_text(entry)),
        "volume " + esc(volume) if volume else "",
        str(year_of(entry)) if year_of(entry) else "",
    ]
    line = ", ".join(part for part in parts if part)
    if line:
        line += "."
    if note:
        line += " " + esc(note if note.startswith("(") else "(" + note + ")")
    return line


# ---------- HTML ----------

# (slug, heading) in the order of the old "by publication type" view
SECTIONS = [("books", "Books"),
            ("articles", "Refereed Articles and Book Chapters"),
            ("conferences", "Refereed Conference Papers"),
            ("workshops", "Refereed Workshop Papers"),
            ("other", "Other Publications")]


def esc(text):
    return html.escape(text, quote=False)


def attr(text):
    return html.escape(text, quote=True)


def section_of(entry):
    if entry.kind in ("book", "inbook"):
        return "books"
    if entry.kind in ("article", "incollection"):
        return "articles"
    if entry.kind.startswith(("inproceedings", "conference")):   # also "InProceedingsunknown"
        venue = clean(entry.fields.get("booktitle", "")).lower()
        return "workshops" if "workshop" in venue or "workshop" in entry.tags else "conferences"
    return "other"


def item_html(entry, number, with_id):
    """One <li>, written for the depth it has inside <div><section><ol>."""
    url = clean_url(entry.fields.get("url", ""))
    title = esc(clean(entry.fields.get("title") or entry.key))
    lines = []
    if url:
        lines.append('<a class="pub-title" href="%s">%s</a>' % (attr(url), title))
    else:
        lines.append('<span class="pub-title">%s</span>' % title)
    lines.append(citation_html(entry))
    if url:
        lines.append('<span class="pub-links"><a href="%s">[pdf]</a></span>' % attr(url))
    lines.append('<details class="pub-bib"><summary>[bib]</summary><pre>%s</pre></details>'
                 % esc(entry.raw))
    ident = ('id="%s"' if with_id else 'data-key="%s"') % attr(entry.key)
    return ('      <li class="pub" %s data-tags="%s">\n'
            '        <span class="pub-num">[%d]</span>\n'
            '        <div class="pub-body">\n'
            '%s'
            '        </div>\n'
            '      </li>\n') % (ident, attr(" ".join(entry.tags)), number,
                                 "".join("          %s\n" % line for line in lines if line))


def group_html(slug, heading, items, with_id):
    lis = "".join(item_html(entry, number, with_id) for entry, number in items)
    return ('  <section class="pub-group" data-group="%s">\n'
            '    <h3>%s</h3>\n'
            '    <ol class="pubs">\n%s'
            '    </ol>\n'
            '  </section>\n') % (attr(slug), esc(heading), lis)


def by_year_html(numbered):
    groups = ""
    for year, items in groupby(numbered, key=lambda pair: year_of(pair[0])):
        label = str(year) if year else "Undated"
        groups += group_html(label, label, list(items), True)
    return '<div id="pubs-by-year" class="pub-list">\n%s</div>\n' % groups


def by_type_html(numbered):
    groups = ""
    for slug, heading in SECTIONS:
        items = [pair for pair in numbered if section_of(pair[0]) == slug]
        groups += group_html(slug, heading, items, False)
    return '<div id="pubs-by-type" class="pub-list" hidden>\n%s</div>\n' % groups


def render(bib_path):
    entries = parse_bib(Path(bib_path).read_text(encoding="utf-8"))
    ordered = sorted(entries, key=lambda entry: (year_of(entry), entry.key), reverse=True)
    numbered = [(entry, len(ordered) - i) for i, entry in enumerate(ordered)]
    return by_year_html(numbered) + by_type_html(numbered)
