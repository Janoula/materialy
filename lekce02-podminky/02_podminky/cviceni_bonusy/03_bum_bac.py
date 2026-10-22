# Bonus 3 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Bum-Bác pro jedno číslo.
#     Zeptej se na číslo a vypiš:
#       - "BumBác", když je dělitelné třemi i pěti zároveň,
#       - "Bum", když je dělitelné jen třemi,
#       - "Bác", když je dělitelné jen pěti,
#       - jinak samotné číslo.

cislo = int(input("Číslo:"))
zbytek3 = cislo % 3
if zbytek3 == 0:
    zbytek5 = cislo % 5
    if zbytek5 == 0:
        print("Bumbác")
    else:
        print("Bum")
else:
    zbytek5 = cislo % 5
    if zbytek5 == 0:
        print("Bác")
    else:
        print(cislo)