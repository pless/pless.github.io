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

## Local links that were already broken on the GWU site
- teaching: `240/index.html`, `classes/555/project2highlights.html`, `classes/555/project3highlights.html`
- classes/ComputerVision: `Lectures/lecture12_introRecognition.pptx`, `Lectures/lecture13_recognitionIntro.pptx`
- publications: `papers/georg2008cvpr.pdf` (georgCVPR2008), `papers/pless_Omni.pdf` (plessOmni), `../omnivis2003/program.html` (omnivis03)

## Content that looks out of date or wrong (kept as it is)
- Home: the CVPR 2024 update; typos "micro-satellites a visual depiction", "publics ability", a stray quote after "Sorghum".
- Join my group: the text is about WashU (Media and Machines Lab, the WashU graduate program).
- Students: Yu Wu is a current MS student with "MS Dec. 2024"; "Graduated May. 2024 2023" (Xiaotong Liu); the name "Ali Bukys" against "Avi Bukys", "Devorah Langsham" against "Langsam", "Justine-louise" against "Justine-Louis"; Nathan Jacobs's link goes to Kentucky but the note says WashU.
- Awards: "NathanJacobs", "cloudly".
- Code: "2Mbyes"; the zip sizes in the text (12 KB, 2 MB) do not match the files (9 KB, 8 KB). The Google Code links point to a service that closed in 2016.
- CV: `longCVbibtex.pdf` is from April 2019.
- Course pages: "Algorihtms", "It's advantages" (3212 syllabus).

## External links that do not answer (checked 2026-10-28)
56 dead (404, 410, 400, 5xx, or no such host):

- `000` http://amos.cse.wustl.edu (index.html)
- `404` http://citeseer.ist.psu.edu/64916.html (publications.html)
- `404` http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.64.7864&rep=rep1&type=pdf (publications.html)
- `404` http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.76.2399&rep=rep1&type=pdf (publications.html)
- `404` http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.80.7118&rep=rep1&type=pdf (publications.html)
- `000` http://code.google.com/p/image-car-annotation/ (code.html)
- `400` http://cs.uky.edu/~jacobs/ (people.html)
- `400` http://cs.uky.edu/~jacobs/papers/icassp_2010/jacobs2010csmotion.pdf (publications.html)
- `400` http://cs.uky.edu/~jacobs/papers/jacobs2010depthfromclouds.pdf (publications.html)
- `404` http://cse.wustl.edu/Research/Lists/Technical%20Reports/Attachments/859/sheet_tracking_tr.pdf (publications.html)
- `404` http://cse.wustl.edu/graduateprograms/Pages/default.aspx (opportunities.html)
- `404` http://engineering.wustl.edu/magazine/RobertPless.aspx (awards.html)
- `404` http://ieeexplore.ieee.org/xpl/abs_free.jsp?arNumber=1371607 (publications.html)
- `502` http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=5456373 (publications.html)
- `000` http://projectrephoto.com (index.html)
- `404` http://research.engineering.wustl.edu/~abramsa/ (people.html)
- `404` http://research.engineering.wustl.edu/~abramsa/papers/webcams_in_context.pdf (publications.html)
- `404` http://research.engineering.wustl.edu/~mdixon/publications/icdsc2009.pdf (publications.html)
- `404` http://research.engineering.wustl.edu/~mdixon/publications/wmvc2008.pdf (publications.html)
- `404` http://research.engineering.wustl.edu/~miskellk/ (people.html)
- `404` http://research.engineering.wustl.edu/~pless/canIDoResearch.html (opportunities.html)
- `000` http://rsif.royalsocietypublishing.org/content/11/100/20140685 (publications.html)
- `000` http://rsif.royalsocietypublishing.org/content/early/2010/05/25/rsif.2010.0210.abstract (publications.html)
- `000` http://www.cens.ucla.edu/sensys03/proceedings/p28-wang.pdf (publications.html)
- `404` http://www.cfar.umd.edu/~jneumann/Papers/bake01f.pdf (publications.html)
- `404` http://www.cs.wustl.edu/MediaAndMachines/publications/papers/VIObjCap2003.pdf (publications.html)
- `404` http://www.cs.wustl.edu/MediaAndMachines/publications/papers/VIPaper2003.pdf (publications.html)
- `404` http://www.cs.wustl.edu/MediaAndMachines/publications/papers/zhang2005levelsets.pdf (publications.html)
- `404` http://www.cs.wustl.edu/~jacobsn/papers/dixon_POCV06.pdf (publications.html)
- `404` http://www.cs.wustl.edu/~jacobsn/papers/wmvc_2007/jacobs_WMVC07.pdf (publications.html)
- `404` http://www.cs.wustl.edu/~msd2/ (people.html)
- `404` http://www.cs.wustl.edu/~msd2/publications/mvap2010.pdf (publications.html)
- `404` http://www.cs.wustl.edu/~pless/200/ (teaching.html)
- `404` http://www.cs.wustl.edu/~pless/441/ (teaching.html)
- `404` http://www.cs.wustl.edu/~pless/546/ (teaching.html)
- `404` http://www.cs.wustl.edu/~pless/559 (teaching.html)
- `404` http://www.cs.wustl.edu/~pless/classes/555/ (teaching.html)
- `404` http://www.cs.wustl.edu/~pless/halloffame/richardspage.html (teaching.html)
- `404` http://www.cs.wustl.edu/~pless/halloffame/shorteningzones.html (teaching.html)
- `404` http://www.cs.wustl.edu/~zql (people.html)
- `000` http://www.cse.seas.wustl.edu/techreportfiles/getreport.asp?431 (publications.html)
- `404` http://www.cse.wustl.edu/~astylianou/papers/Finding_Jane_Doe.pdf (publications.html)
- `404` http://www.cse.wustl.edu/~astylianou/papers/featuresOverTime.pdf (publications.html)
- `404` http://www.cse.wustl.edu/~jacobsn/papers/cvpr_2007/jacobs2007amos.pdf (publications.html)
- `404` http://www.cse.wustl.edu/~jacobsn/papers/iv_2009/jacobs09webcamdata.pdf (publications.html)
- `404` http://www.cse.wustl.edu/~jacobsn/papers/vssn_2006/jacobs_vssn06.pdf (publications.html)
- `404` http://www.cse.wustl.edu/~mgeorg/index.html (people.html)
- `404` http://www.cse.wustl.edu/~msd2/publications/dixon2007iros.pdf (publications.html)
- `404` http://www.cse.wustl.edu/~schillebeeckxi/ (people.html)
- `404` http://www.cse.wustl.edu/~xing/docs/f1568951884-xing.pdf (publications.html)
- `404` http://www.cse.wustl.edu/~xing/docs/tpds05.pdf (publications.html)
- `404` http://www.foxnews.com/us/2013/06/23/who-was-new-technology-brings-hope-to-identifying-headless-girl/ (awards.html)
- `410` http://www.gizmag.com/tissue-strain-algorithm-wustl/33607/ (awards.html)
- `500` http://www.jstage.jst.go.jp/article/ipsjtcva/1/0/83/_pdf (publications.html)
- `000` http://www.springerlink.com/content/l43k866072713057/ (publications.html)
- `000` http://www2.seas.wustl.edu/~astylianou/ (people.html)

16 more refuse automated checks (403 or 999). They probably work in a browser:

- `403` http://asadl.org/jasa/resource/1/jasman/v91/i5/p2637_s1?isAuthorized=no (publications.html)
- `403` http://cacm.acm.org/news/94861-clouds-add-depth-to-computer-landscapes/fulltext (awards.html)
- `403` http://cs.engr.uky.edu/~jacobs/papers/wacv_2008/jacobs08geoorient.pdf (publications.html)
- `403` http://dl.acm.org/citation.cfm?id=2811941&CFID=562586363&CFTOKEN=60745233 (publications.html)
- `403` http://openscholarship.wustl.edu/cgi/viewcontent.cgi?article=1002&context=brown_facpubs (publications.html)
- `403` http://portal.acm.org/citation.cfm?id=1116041 (publications.html)
- `403` http://portal.acm.org/citation.cfm?id=648247.753974 (publications.html)
- `403` http://www.cs.ucla.edu/~jurgens (people.html)
- `406` http://www.newscientist.com/article/dn18449-realtime-webcam-images-painted-onto-google-earth.html (awards.html)
- `403` http://www.pnas.org/content/111/12/4602.short (publications.html)
- `403` http://www.pnas.org/content/112/51/E7148.abstract (publications.html)
- `403` http://www.pnas.org/content/early/2010/10/04/1008737107.abstract (publications.html)
- `403` http://www3.interscience.wiley.com/journal/123210660/abstract (publications.html)
- `403` https://teachingcenter.wustl.edu/programs/faculty/teaching-awards/emerson/ (awards.html)
- `999` https://www.linkedin.com/in/jayne-tucek/ (people.html)
- `999` https://www.linkedin.com/pub/zachary-freudenburg/6a/a92/993 (people.html)
