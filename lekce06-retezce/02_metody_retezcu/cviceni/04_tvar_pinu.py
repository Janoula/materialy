# Cvičení 4 – Metody řetězců
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na PIN a zkontroluj, jestli má správný tvar: přesně čtyři
#    znaky a všechny číslice. Vypiš, jestli je v pořádku.
#    Mezery navíc ať nevadí.
#
#    V lekci 5 jsi PINu dávala tři pokusy na uhodnutí. Tady jde o to,
#    jestli vůbec vypadá jako PIN.

pin = input("Zadej čtyřmístný pin: ").strip()
def je_ze4(pin, delka):
    return len(pin) == int(delka)

if pin.isdigit():
    if je_ze4(pin, "4"):
        print("Tohle může být pin.")
    else:
        print("Zadej pouze 4 čísla.")     


