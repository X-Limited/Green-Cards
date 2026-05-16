
# ============================================
# GREEN CARDS PDF AUTOMATION
# ============================================
#
# Funkce:
# - načte PDF balík zelených karet
# - načte Excel mapování SPZ -> uživatel
# - najde SPZ v PDF stránkách
# - rozdělí PDF na jednotlivé soubory
# - pojmenuje soubory podle uživatele a SPZ
#
# Repository archive version
# ============================================

PDF_SOUBOR = "Balik_ZK_6667500705.pdf"
EXCEL_SOUBOR = "Sesit1.xlsx"
VYSTUPNI_SLOZKA = "vystup_zk"
START_PAGE = 23

print("Green Cards automation script archive version")
