# Bonus 3 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš program, který se pořád dokola ptá, co má dělat:
#
#      kostka     zeptá se, kolikrát hodit, a tolikrát hodí kostkou
#      pozpatku   zeptá se na slovo a vypíše ho pozpátku
#      konec      program skončí
#
#    Odpověď uprav tak, aby prošlo i "KOSTKA" nebo "  konec  ".
#    Ošetři prázdný vstup i počet hodů, který není číslo.
#    Na cokoli jiného vypiš, že takovou volbu neznáš, a zeptej se znovu.
#    Na první řádek patří:  from random import randrange

from random import randrange

while True:
    akce = input("Co mám dělat (kostka/pozpatku/konec)? ")
    akce = akce.strip().lower()
    if akce == "kostka":
        kol = input("Kolikrát mám hodit? ").strip()
        if kol.isdigit():
            for hod in range(1,(int(kol) + 4)):
                cislo = randrange(1,7)
                print(cislo)
        else:
            print("Tohle není číslo.")
    elif akce == "pozpatku":
        slovo = input("Zadej slovo: ").strip().lower()
        print(slovo[::-1])
        continue
    elif akce == "konec":
        break
    else:
        print(f"Tohle ({akce}) neznám, zkus to znova.")
        continue