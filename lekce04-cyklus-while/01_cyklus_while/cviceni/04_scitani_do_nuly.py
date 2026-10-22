# Cvičení 4 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel postupně zadává čísla. Sčítej je. Jakmile zadá 0,
#    přestaň se ptát a vypiš celkový součet.

soucet = 0
cislo = float(input("Číslo: "))
while cislo != 0:
    soucet = soucet + cislo
    cislo = float(input("Číslo: "))
print("Součet:", soucet)

