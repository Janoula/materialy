# Cvičení 2 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci je_plnoleta(vek), která vrátí True, nebo False.
#    Zeptej se uživatele na věk a podle výsledku vypiš
#    "Můžeš dál." nebo "Ještě ne.".

def je_plnoleta(vek):
    if vek > 17:
        return print("Můžeš dál.")
    else:
        return print("Ještě ne.")

vek = int(input("Věk: "))
je_plnoleta(vek)

