# Bonus 1 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Trojúhelník z hvězdiček. Uživatel zadá výšku a ty vypiš
#     trojúhelník, kde první řádek má jednu hvězdičku, druhý dvě atd.:
#     *
#     **
#     ***

vyska = int(input("Výška: "))
for i in range(1, vyska + 1):
    print("*" * i)
print()