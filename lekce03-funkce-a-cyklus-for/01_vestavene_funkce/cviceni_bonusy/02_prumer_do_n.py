# Bonus 2 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Průměr od 1 do N. Uživatel zadá číslo N. Vypiš průměr všech čísel
#     od 1 do N (součet čísel vyděl jejich počtem).

cislo = int(input("Cislo: "))
prumer = sum(range(1, cislo + 1)) / cislo
print(prumer)

