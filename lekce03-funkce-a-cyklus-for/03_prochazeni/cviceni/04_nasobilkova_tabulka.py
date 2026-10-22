# Cvičení 4 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Násobilková tabulka. Pomocí vnořených cyklů vypiš tabulku 4x4,
#    kde na řádku R a sloupci S je jejich součin:
#        1 2 3 4
#        2 4 6 8
#        3 6 9 12
#        4 8 12 16
#    Jak pojmenuješ obě proměnné cyklu? Zamysli se, ať dávají smysl.

r = int(input("Počet řádků: "))
s = int(input("Počet sloupců: "))
for r in range(1, r + 1):
    for s in range(1, s + 1):
        print(r * s, end = " ")
    print()
    
