# Bonus 1 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá celkovou cenu útraty a počet lidí. Vypiš, kolik
#     zaplatí každý, zaokrouhleno na dvě desetinná místa.

utrata = float(input("Útrata: "))
osob = int(input("Počet osob: "))

kazdy = round(utrata / osob, 2)
print(kazdy)

