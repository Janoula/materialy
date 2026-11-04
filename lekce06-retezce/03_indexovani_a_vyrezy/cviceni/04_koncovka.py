# Cvičení 4 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na jméno souboru a vypiš, jestli je to obrázek,
#    tedy jestli končí na .png

soubor = input("Zadej název souboru: ")

if soubor.endswith(".png"):
    print("Je to obrázek.")
else:
    print("Není to obrázek.")
