# Port review, 2026-10-28

This note lists what the first build of pless.github.io changed from www2.seas.gwu.edu/~pless/. It also lists what the port kept, although it is broken or out of date. The items in those lists need Robert's decision.

## Changes from the GWU site
- Layout: centered, at most 1060 px wide; one column on phones. Darker link green (WCAG AA contrast); the menu marks the current page.
- Publications: a static list made from `pubs/plessRefs.bib` (150 entries, same numbers and order as before). The topic views use the tags in the `annote` field instead of bibtexbrowser's free-text search. The free-text search put 7 papers into "Machine Learning" only because of "html" or "ml" inside a URL or a name (for example "Fasting protects mice…"). The new ML view has 46 papers instead of 53; the other views have the same papers as before.
- `pubs/plessRefs.bib`: added `annote={social}` to `counts2018characterizing` ("Characterizing the Visual Social Media Environment of Eating Disorders"). The old social view showed it only because its title has the word "social".
- [bib] opens the BibTeX entry in place; `publications.html#KEY` replaces `bibtexbrowser.php?key=KEY`.
- Students: a name is a button (or a link to the person's homepage); hover, keyboard focus, or a tap shows the photo and note. The photo box stays at the top of the screen while the lists scroll.
- Markup repairs (the text did not change):
  - unclosed and stray tags on the teaching, students and home pages;
  - two JavaScript string errors on the students page (a hover on Jonathan Cannon or Derek Lefever showed nothing);
  - three names outside their links (Sutton Howell, Xuqing (Ken) Zhou, Tang Li);
  - a stray `A` after the PDF URL of `stylianou2021classification`;
  - a comma instead of "and" in the authors of `WACVVis2019`;
  - the malformed bib link on the code page;
  - the syllabus link to provost.gwu.edu, which had no `https://`.
- Removed the Google Analytics `urchin.js` code (the service no longer exists).
- Ian Simon's photo (`webImages/ian.jpg`) was already missing; he shows the default group image. `webImages/emilyFeder.jpeg` was made smaller (3648 to 600 px wide). `webImages/pless-280.jpg` is a small copy of the portrait for the left column.

## Broken links
Replaced on 2026-10-28 by working copies: see `2026-10-28-dead-links.md`. Three local links that were already broken on the GWU site had no copy anywhere, and Robert had them removed.

## Content that looks out of date or wrong (kept as it is)
- Home: the CVPR 2024 update; typos "micro-satellites a visual depiction", "publics ability", a stray quote after "Sorghum".
- Join my group: the text is about WashU (Media and Machines Lab, the WashU graduate program).
- Students: "Graduated May. 2024 2023" (Xiaotong Liu); the name "Ali Bukys" against "Avi Bukys", "Devorah Langsham" against "Langsam", "Justine-louise" against "Justine-Louis".
- Awards: "NathanJacobs", "cloudly".
- Code: "2Mbyes"; the zip sizes in the text (12 KB, 2 MB) do not match the files (9 KB, 8 KB).
- CV: `longCVbibtex.pdf` is from April 2019.
- Course pages: "Algorihtms", "It's advantages" (3212 syllabus).
