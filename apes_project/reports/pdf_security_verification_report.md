# PDF security verification report

Protected PDFs: AES-256 (PDF 2.0 /AESV3), empty user password (opens without a password for students), random owner password (not recorded), all permission bits cleared: no printing, no copying or text extraction by compliant readers, no editing, no annotation, no form filling.

| File | Encrypted | Opens without password | Pages readable | AES-256 marker | Permission flag /P |
|---|---|---|---|---|---|
| APES_Complete_Study_Guide_Protected.pdf | True | True | 290 | True | 0 |
| APES_Classified_Practice_4_Predicted_Exams_Protected.pdf | True | True | 348 | True | 0 |
| APES_Complete_Solutions_Protected.pdf | True | True | 145 | True | 0 |
| APES_College_Board_Questions_And_Solutions_Protected.pdf | True | True | 126 | True | 0 |

Limits (stated honestly): PDF protection is advisory. It does not prevent screenshots, photographing the screen, or OCR, and some non-compliant tools ignore the permission flags. The fonts in all PDFs are embedded (Liberation Serif, the metric-compatible equivalent of Times New Roman, because Times New Roman itself is not installed on the production machine; the DOCX files specify Times New Roman and will use it on Windows/macOS).