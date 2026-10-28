# pless.github.io

## What this is
Robert Pless's personal website. GitHub Pages serves it at https://pless.github.io from the public repository github.com/pless/pless.github.io. It is a port of the PHP site www2.seas.gwu.edu/~pless/ to static files (2026-10-28). The text comes from that site. The look follows that site, with a layout that also works on phones.

## Where things live
- **Current status:** see STATUS.md
- **Pages:** `index.html` (home), `people.html` (students), `teaching.html`, `publications.html`, `awards.html` (awards/press), `opportunities.html` (join my group), `code.html`. The names are the GWU names with `.php` changed to `.html`.
- **Course pages** (no left column): `3212/` (Algorithms), `classes/ComputerVision/` (with the lecture slides).
- **Files:** `papers/` (paper PDFs), `webImages/` (photos), `code/` (zip files), `longCVbibtex.pdf` (CV), `pubs/plessRefs.bib` (all publications). They have the same paths as on the GWU site, so the relative links in the BibTeX file work as they are.
- **Style and scripts:** `style.css` (all pages), `people.js` (the student photos), `publications.js` (the publication views).
- **Build:** `tools/build.py`; `tools/sidebar.html` (the shared left column); `tools/bib2html.py` (the publication list).
- **Notes:** `notes/` (dated files).

## How to change the site
- Text of a page: edit the page's `.html` file, inside `<main>`.
- Left column or menu: edit `tools/sidebar.html`, then run `python3 tools/build.py`.
- New paper: add the entry to `pubs/plessRefs.bib`, put the PDF in `papers/`, set `url={papers/NAME.pdf}`, then run `python3 tools/build.py`. Topic tags go in the `annote` field: `selected`, `geometry`, `ML`, `social`, `ugrad`.
- `pubs/plessRefs.bib` changed on GitHub (an upload or a web edit): the publications page does not change by itself, because GitHub Pages does not run the build. Pull, run `python3 tools/build.py`, then commit and push `publications.html`.
- Look at the result: run `python3 -m http.server 8790` in this folder, then open http://localhost:8790.
- Publish: commit and push to `main`. GitHub Pages shows the new version after about a minute.

## Key design decisions
- Plain static HTML. No framework and no Jekyll (`.nojekyll`): the files in the repository are the files on the site, so a local preview shows exactly what visitors see.
- No templates for page text. `tools/build.py` writes only two regions, between marker comments: the left column (`<!-- begin sidebar -->`) in each top-level page, and the publication list (`<!-- begin publications -->`) in `publications.html`. Do not edit inside these regions by hand: the next build replaces them.
- The publication list is static HTML, so it reads without JavaScript and search engines see it. `publications.js` only switches views: `publications.html#selected` (also `#geometry`, `#ML`, `#social`, `#ugrad`, `#type`, `#all`) opens a view, and `publications.html#<bibkey>` opens one entry. These links replace the old `publications.php?search=` and `bibtexbrowser.php?key=` links.
- The topic views use only the tags in the `annote` (also `annotation`, `annotations`) field. The GWU site used bibtexbrowser's free-text search, which also matched "ml" inside "html" in URLs; see `notes/2026-10-28-port-review.md`.
- `tools/bib2html.py` keeps the old numbers and order: year descending, then BibTeX key descending.
- The PDFs, photos, slides and code are in the repository (about 330 MB), so the site does not depend on the GWU server. Each file must stay under 100 MB (GitHub limit). Do not use Git LFS: GitHub Pages does not serve LFS files.
- The build uses only the Python 3 standard library.

## Conventions
- The look: gray page, gray cards, a left column with photo, contact and menu, section headings with an olive top rule, green links. The colors are CSS variables at the top of `style.css`. Link colors pass WCAG AA contrast on the card gray.
- Links between pages of this site are relative.
- Keep the page names: other sites link to them.
- Keep the text of the GWU site unless Robert asks for a change.

## Working agreement
When you create a markdown file, classify it first:
- durable reference → add to this file (or a file it links to)
- current status → update STATUS.md, don't make a new status file
- investigation notes → notes/ with a dated filename (YYYY-MM-DD-topic.md)

Don't create new top-level .md files for status. At the end of a work session, update STATUS.md for the task we worked on.
