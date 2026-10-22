# Cvičení 1 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Analýza věty. Uživatel zadá větu. Projdi ji znak po znaku a vypiš
#    počet znaků, počet samohlásek, počet mezer a počet slov ve větě.
#    (Počet slov = počet mezer + 1.)

veta = input("Zadej větu: ")
znaky = 0
samohlasky = 0
mezery = 0
slova = 0
for object in veta:
    znaky = znaky + 1
    if object in "aeiouy":
        samohlasky = samohlasky + 1
    elif object in " ":
        mezery = mezery + 1
        slova = mezery + 1

print("Znaky: ", znaky)
print("Mezery: ", mezery)
print("Samohlasky: ", samohlasky)
print("Slova: ", slova)