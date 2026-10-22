# Bonus 1 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Sudé, nebo liché?
#     Zeptej se uživatele na celé číslo a vypiš, jestli je sudé, nebo liché.

cislo = int(input("Zadej libovolné celé číslo: "))
zbytek = cislo % 2
if zbytek == 1:
    print("Je to liché číslo.")
else:
    print("Číslo je sudé.")
