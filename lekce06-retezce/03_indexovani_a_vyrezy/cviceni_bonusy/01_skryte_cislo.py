# Bonus 1 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# Vypiš číslo karty tak, aby byly vidět jen poslední čtyři číslice.
#    Zbytek nahraď hvězdičkami, ať jich je přesně tolik jako
#    skrytých číslic.

cislo = "4539447788"

delka_hvezd = len(cislo) - 4
print((delka_hvezd * "*")+cislo[-4:])


