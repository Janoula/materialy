# Cvičení 3 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# V proměnné datum je text ve tvaru rok-měsíc-den. Vypiš ho česky,
#    tedy ve tvaru:  17. 10. 2026

datum = "2026-10-17"

print(f"{datum[-2:]}. {datum[-5:-3]}. {datum[:-6]}")
