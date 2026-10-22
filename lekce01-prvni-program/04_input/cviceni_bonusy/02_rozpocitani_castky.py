# Bonus 2 – Vstup od uživatelky
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na částku a na počet lidí.
#     Vypiš, kolik zaplatí každý a kolik korun zbyde.

utrata = int(input("Kolik je dneska útrata? "))
osob = int(input("A kolik vás dneska je? "))
print("Tak to vychází na každého", utrata  // osob, "Kč a ještě", utrata % osob, "Kč zbude k doplacení." )
