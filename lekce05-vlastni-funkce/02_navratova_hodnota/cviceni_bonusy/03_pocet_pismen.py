# Bonus 3 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci spocitej_pismeno(slovo, pismeno), která vrátí,
#     kolikrát se písmeno ve slově objeví.
#     spocitej_pismeno("kolotoč", "o") vrátí 3.
#     Nechej si zadat slovo i písmeno od uživatele a výsledek vypiš.

def spocitej_pismeno(slovo, pismeno):
    stav = 0
    for znak in slovo:
        if znak == pismeno:
            stav = stav + 1
        else:
            continue
    print("Počet", pismeno, "v", slovo, "je", stav, ".")

slovo = input("Zadej slovo: ")
pismeno = input("Jaké písmeno chceš spočítat? ")
spocitej_pismeno(slovo, pismeno)


