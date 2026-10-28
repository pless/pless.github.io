# STATUS — pless.github.io

Last updated: 2026-10-28

## Project snapshot
Static port of www2.seas.gwu.edu/~pless/ for GitHub Pages at https://pless.github.io. First version published 2026-10-28.

---

## Task: Port the GWU site   [active]
Tab/folder: Claude Code desktop; folder ~/projects/pless-webpage

- **Goal:** pless.github.io shows the content of the GWU site in the same style, and works on phones.
- **Now:** first version live at https://pless.github.io since 2026-10-28, from the public repo github.com/pless/pless.github.io (GitHub Pages, branch `main`, folder `/`). All 119 site files load there, and the publication views and student photos work. Later the same day: students added and moved at Robert's request, and 68 of the 80 broken links replaced by working copies (`notes/2026-10-28-dead-links.md`); the 3 links with no copy anywhere removed. Publications rebuilt from Robert's new `pubs/plessRefs.bib` (156 entries, uploaded on GitHub), with the link fixes applied to it again.
- **Next:** Robert reviews `notes/2026-10-28-port-review.md` (out-of-date text, typos) and `notes/2026-10-28-dead-links.md` (possible errors in the bib file).
- **Blockers:** none.
- **Key files:** tools/build.py, style.css, pubs/plessRefs.bib

---

## Parking lot
- Robert to decide: a GitHub Action that rebuilds the publications page whenever `pubs/plessRefs.bib` changes. Today a change to the bib file shows on the site only after someone runs `python3 tools/build.py` and pushes.
- Update the CV (`longCVbibtex.pdf` is from 2019) and the "join my group" text (it is about WashU).
