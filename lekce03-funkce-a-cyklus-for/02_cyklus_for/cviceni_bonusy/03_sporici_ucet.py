# Bonus 3 – Cyklus for
# Doplň kód pod zadání a soubor spusť (Run).

# Uživatel zadá počáteční částku na spořicím účtu. Úrok je 5 % ročně.
#     Spočítej cyklem, kolik na účtu bude po deseti letech
#     (každý rok se částka vynásobí 1.05), a výsledek vypiš.

ucet = int(input("Stav účtu: "))
for i in range(10):
    ucet = ucet * 1.05
print(round(ucet, 2))
