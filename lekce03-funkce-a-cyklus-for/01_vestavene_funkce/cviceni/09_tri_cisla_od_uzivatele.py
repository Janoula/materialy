# Cvičení 9 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se uživatele na tři čísla (klidně i záporná) a vypiš,
#    jak velké je to největší z nich bez ohledu na znaménko.
#    Např. z čísel -20, 5 a 12 je největší velikost 20.

a = abs(int(input("Prvni:")))
b = abs(int(input("Prvni:")))
c = abs(int(input("Prvni:")))
print(max(a, b, c))
