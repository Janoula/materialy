# Bonus 2 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Největší ze tří.
#     Máš tři čísla. Zjisti a vypiš to největší z nich.
a = 30
b = 30
c = 30


if a > b:
    if a > c:
        print(a)
    else:
        print(c)
elif b > c:
    if b > a:
        print(b)
    else:
        print(a)
else:
    print(c)
