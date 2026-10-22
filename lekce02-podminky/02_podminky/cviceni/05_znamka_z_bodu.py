# Cvičení 5 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na počet bodů z testu (0 až 100) a vypiš známku:
#    90 a víc → 1, 75 a víc → 2, 60 a víc → 3, 40 a víc → 4,
#    jinak → 5.

body = int(input("Kolik jsi získal bodů v testu? "))
if body >= 90:
    print("Výborně.")
elif body >= 75:
    print("Chvalitebně.")
elif body >= 60:
    print("Dobře.")
elif body >= 40:
    print("Dostatečně.")
else:
    print("Nedostatečně.")
