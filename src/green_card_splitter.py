import os
import re
import pandas as pd
import pdfplumber
from PyPDF2 import PdfReader, PdfWriter

PDF_SOUBOR = "Balik_ZK_6667500705.pdf"
EXCEL_SOUBOR = "Sešit1.xlsx"
VYSTUPNI_SLOZKA = "output"
START_PAGE = 23

os.makedirs(VYSTUPNI_SLOZKA, exist_ok=True)

df = pd.read_excel(EXCEL_SOUBOR)

SPZ_SLOUPEC = "SPZ"
UZIVATEL_SLOUPEC = "Uživatel"

mapa_uzivatelu = {}

for _, row in df.iterrows():
    spz = str(row[SPZ_SLOUPEC]).strip().upper()
    uzivatel = str(row[UZIVATEL_SLOUPEC]).strip()
    mapa_uzivatelu[spz] = uzivatel

spz_regex = r"\\b\\d[A-Z0-9]{1,2}\\d{4}\\b|\\b[A-Z]{2,3}\\d{4}\\b"

reader = PdfReader(PDF_SOUBOR)

with pdfplumber.open(PDF_SOUBOR) as pdf:

    for i in range(START_PAGE - 1, len(pdf.pages)):

        page = pdf.pages[i]
        text = page.extract_text()

        if not text:
            continue

        text_upper = text.upper()

        nalezene_spz = re.findall(spz_regex, text_upper)

        if not nalezene_spz:
            continue

        spz = nalezene_spz[0].replace(" ", "")

        uzivatel = mapa_uzivatelu.get(spz, "NEZNAMY")

        uzivatel_safe = re.sub(r'[\\\\/*?:\"<>|]', "", uzivatel)

        vystupni_soubor = f"{spz}_{uzivatel_safe}.pdf"

        vystupni_cesta = os.path.join(
            VYSTUPNI_SLOZKA,
            vystupni_soubor
        )

        writer = PdfWriter()
        writer.add_page(reader.pages[i])

        with open(vystupni_cesta, "wb") as f:
            writer.write(f)

        print(f"Uloženo: {vystupni_soubor}")

print("HOTOVO")
