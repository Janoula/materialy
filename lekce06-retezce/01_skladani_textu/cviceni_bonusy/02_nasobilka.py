# Bonus 2 – Skládání textu
# Doplň kód pod zadání a soubor spusť (Run).

# V lekci 3 jsi vnořenými cykly vypsala násobilkovou tabulku. Sloupce
#    se v ní rozjely, protože dvojciferná čísla jsou širší:
#
#        1 2 3 4
#        2 4 6 8
#        3 6 9 12
#        4 8 12 16
#
#    Napiš ji znovu tak, aby čísla byla pod sebou. Tabulku rovnou
#    zvětši na 10x10, ať je rozdíl pořádně vidět.
#
#    Vnořené cykly i print s end znáš z lekce 3. Nové je jen to,
#    kolik místa každému číslu dáš.

r = int(input("Počet řádků: "))
s = int(input("Počet sloupců: "))
soucin = r * s
cifer = max(len(str(r)), len(str(s)), len(str(soucin)))
print(cifer)
misto = cifer + 2
for r in range(1, r + 1):
    for s in range(1, s + 1):
        print(f"{r * s:{misto}}", end = " ")
    print()
    


