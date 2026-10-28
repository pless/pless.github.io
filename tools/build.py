#!/usr/bin/env python3
"""Build step for pless.github.io. Python 3 standard library only.

It fills two kinds of marked regions in the top-level pages:

  <!-- begin sidebar --> ... <!-- end sidebar -->
      The shared left column, copied from tools/sidebar.html, with the
      current page marked in the menu (aria-current="page").

  <!-- begin publications --> ... <!-- end publications -->
      (publications.html only) The publication list, made from
      pubs/plessRefs.bib by tools/bib2html.py.

Everything outside the markers is plain HTML: edit it directly.

Usage:
  python3 tools/build.py                  # all pages
  python3 tools/build.py people.html      # only the pages named
"""
import re
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent
ROOT = TOOLS.parent
PAGES = ["index.html", "people.html", "teaching.html", "publications.html",
         "awards.html", "opportunities.html", "code.html"]


def replace_region(text, name, body, page):
    pattern = re.compile(r"(<!-- begin %s -->\n).*?(<!-- end %s -->)" % (name, name), re.S)
    if not pattern.search(text):
        sys.exit(f"{page}: no '<!-- begin {name} -->' / '<!-- end {name} -->' markers")
    return pattern.sub(lambda m: m.group(1) + body + m.group(2), text, count=1)


def sidebar_for(page, sidebar):
    link = f'<a href="{page}">'
    return sidebar.replace(link, f'<a href="{page}" aria-current="page">')


def main(pages):
    sidebar = (TOOLS / "sidebar.html").read_text(encoding="utf-8")
    for page in pages:
        if page not in PAGES:
            sys.exit(f"unknown page {page}; pages are: {' '.join(PAGES)}")
        path = ROOT / page
        text = path.read_text(encoding="utf-8")
        new = replace_region(text, "sidebar", sidebar_for(page, sidebar), page)
        if page == "publications.html":
            sys.path.insert(0, str(TOOLS))
            import bib2html
            new = replace_region(new, "publications",
                                 bib2html.render(ROOT / "pubs" / "plessRefs.bib"), page)
        if new != text:
            path.write_text(new, encoding="utf-8")
            print("updated", page)


if __name__ == "__main__":
    main(sys.argv[1:] or PAGES)
