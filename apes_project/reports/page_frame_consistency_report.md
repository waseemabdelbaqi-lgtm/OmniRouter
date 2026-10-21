# Page-frame and watermark consistency report

- Frame definition (page-border XML) identical in all four DOCX files: **True**
- Position/size of every anchored frame/watermark picture in the headers identical in all four books: **True**
- Border XML used everywhere: `<w:pgBorders w:offsetFrom="page"><w:top w:val="double" w:sz="12" w:space="20" w:color="7A1424"/><w:left w:val="double" w:sz="12" w:space="20" w:color="7A1424"/><w:bottom w:val="double" w:sz="12" w:space="20" w:color="7A1424"/><w:right w:val="double" w:sz="12" w:space="20" w:color="7A1424"/></w:pgBorders>`
- Frame: double line, #7A1424, 1.5 pt, 20 pt from the page edge on all four sides, with four corner ornaments (#7A1424 / #4A0D14) — one design applied to every section of every book (covers, front matter, content, contact page, back cover).
- Watermark: the official Success4Sure logo (extracted from the company profile / author's artwork, official proportions), 24.6 cm long, rotated 54.7° clockwise so it runs from the TOP-LEFT to the BOTTOM-RIGHT corner along the A4 diagonal, centred on the page, 13% opacity, anchored behind the text in the page header of every section.

## Automated per-page inspection of the final PDFs (rendered at 50 dpi)

| Book | Pages | Pages missing frame | Pages missing watermark | Blank pages | Content touching frame |
|---|---|---|---|---|---|
| Book One — Complete Study Guide | 290 | 0 | 0 | 0 | 0 |
| Book Two — Classified Practice & Four Predicted Exams | 348 | 0 | 0 | 0 | 0 |
| Book Three — Complete Solutions | 145 | 0 | 0 | 0 | 0 |
| Book Four — College Board Questions & Solutions | 126 | 0 | 0 | 0 | 0 |

Method: each page was rendered; the four frame sides were sampled for the maroon double line at the fixed offset; each page's content stream was checked for the watermark raster; blank-page and frame-crowding tests were run on the interior. In addition, sampled pages from every book (covers, contents, unit pages, question pages, exam FRQ pages, solution pages, contact and back covers) were inspected visually.