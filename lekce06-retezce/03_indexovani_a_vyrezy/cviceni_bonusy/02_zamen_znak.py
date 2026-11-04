# Bonus 2 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci zamen, která má na vstupu text, pozici a znak. Vrátí text,
#    který má na té pozici daný znak a jinak zůstane stejný.
#    zamen("palec", 0, "v") vrátí "valec"
#    zamen("valec", 2, "j") vrátí "vajec"

def zamen(slovo, pozice, pismeno):
    return slovo[:pozice -1] + pismeno + slovo[pozice:]

print(zamen("hromada", 7, "y"))
print(zamen("valec", 3, "j"))

