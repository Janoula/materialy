# Cvičení 4 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci zeptej_se_na_slovo(), která se ptá tak dlouho,
#    dokud uživatel nezadá slovo aspoň o třech písmenech, a slovo vrátí.
#    Zavolej ji a výsledek pošli do funkce nadpis, která je připravená níž.

def nadpis(text):
    print(text)
    print("-" * len(text))

def zeptej_se_na_slovo():
    while True:
        slovo = input("Zadej slovo alespoň o třech písmenech: ")
        if len(slovo) > 3:
            return slovo
        else:
            continue

nadpis(zeptej_se_na_slovo())