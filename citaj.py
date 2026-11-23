import pdfplumber

with pdfplumber.open("fakture/Faktura_01_TEST-2026-001.pdf") as pdf:
    for strana in pdf.pages:
        print(strana.extract_text())