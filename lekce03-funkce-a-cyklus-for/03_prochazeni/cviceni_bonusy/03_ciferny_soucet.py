# Bonus 3 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Ciferný součet. Uživatel zadá číslo. Sečti jeho jednotlivé číslice
#     a součet vypiš (třeba z 253 vyjde 2 + 5 + 3 = 10).

soucet = 0
cifra = input("Číslo: ")
for i in cifra:
    soucet = soucet + int(i)
print("Ciferný součet je", soucet)
