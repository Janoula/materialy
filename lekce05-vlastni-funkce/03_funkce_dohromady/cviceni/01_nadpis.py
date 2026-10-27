# Cvičení 1 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci nadpis(text), která vypíše text a pod něj čáru
#    z pomlček dlouhou přesně jako ten text.
#    Vyzkoušej ji na dvou různě dlouhých nadpisech.

def nadpis(text):
    delka = len(text)
    print(text, "-" * delka, sep = "\n")

nadpis("Horní Počernice")
nadpis("Cvičení 4")
