# Cvičení 3 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Statistika čísel. Uživatel zadá, kolik čísel bude zadávat, a pak
#    ta čísla postupně napíše. V jednom průchodu cyklem spočítej a vypiš
#    jejich součet, průměr, největší a nejmenší číslo.
#    Nepoužívej funkce sum, max ani min – spočítej vše sama cyklem.


pocet = int(input("Kolik bude čísel? "))
prvni = int(input("Zadej první číslo: "))
soucet = prvni
nejvetsi = prvni
nejmensi = prvni
for i in range(pocet - 1):
    cislo = int(input("Další číslo: "))
    soucet = soucet + cislo
    if cislo > nejvetsi:
        nejvetsi = cislo
    if cislo < nejmensi:
        nejmensi = cislo
print("Součet: ", soucet)
print("Průměr:", soucet / pocet)
print("Největší: ", nejvetsi)
print("Nejmenší: ", nejmensi)

