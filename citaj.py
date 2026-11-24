import re
import pdfplumber
from pathlib import Path

fajl = list(Path("fakture").glob("*.pdf"))[10]

with pdfplumber.open(fajl) as pdf:
    tekst = "\n".join(strana.extract_text() for strana in pdf.pages)

broj = re.search(r"[A-Z]+-\d{4}-\d{3}", tekst)
datumi = re.findall(r"\d{2}\.\d{2}\.\d{4}\.", tekst)

print("Fajl:", fajl.name)
print("Broj fakture:", broj.group() if broj else "NIJE NAĐEN")
print("Svi datumi:", datumi)
print("Datum izdavanja:", datumi[0] if datumi else "NIJE NAĐEN")