import re
import pdfplumber
from pathlib import Path

fajl = list(Path("fakture").glob("*.pdf"))[4]

with pdfplumber.open(fajl) as pdf:
    tekst = "\n".join(strana.extract_text() for strana in pdf.pages)

broj = re.search(r"[A-Z]+-\d{4}-\d{3}", tekst)
datumi = re.findall(r"\d{2}\.\d{2}\.\d{4}\.", tekst)

print("Fajl:", fajl.name)
print("Broj fakture:", broj.group() if broj else "NIJE NAĐEN")
print("Svi datumi:", datumi)
print("Datum izdavanja:", datumi[0] if datumi else "NIJE NAĐEN")

pibovi = re.findall(r"PIB[^\d]*(\d{9})", tekst)
print("Svi PIB-ovi:", pibovi)
print("PIB dobavljača:", pibovi[0] if pibovi else "NIJE NAĐEN")

iznos = re.search(r"UKUPNO RSD:\s*([\d.]+,\d{2})", tekst)
if iznos:
    tekst_iznosa = iznos.group(1)
    broj = float(tekst_iznosa.replace(".", "").replace(",", "."))
    print("Ukupno (tekst):", tekst_iznosa)
    print("Ukupno (broj):", broj)
else:
    print("Ukupno: NIJE NAĐENO")