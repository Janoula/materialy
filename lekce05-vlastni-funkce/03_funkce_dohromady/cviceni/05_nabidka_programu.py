# Cvičení 5 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš program, který pořád dokola nabízí tři možnosti a zeptá se,
#    co má udělat:
#
#      1 - hodit kostkou
#      2 - pozdravit
#      3 - konec
#
#    Volba 1 hodí kostkou a vypíše, co padlo. Volba 2 se zeptá na jméno
#    a pozdraví ho. Volba 3 program ukončí. Po volbě 1 a 2 se nabídka
#    objeví znovu. Na cokoli jiného program odpoví, že volbu nezná.
#    Použij cyklus while True.
#    Zobrazení nabídky i obě akce napiš jako vlastní funkce.

def nabidka():
    while True:
        print("Nabídka:", "1 - hodit kostkou", "2 - pozdravit", "3 - konec", sep="\n")
        volba = input("Co zvolíš? ")
        if volba == "1":
            kostka()
        elif volba == "2":
            pozdrav()
        elif volba == "3":
            print("konec")
            break
        else:
            print("Tohle neznám. Zkus to znova.")
            continue
        break

     

def kostka():
    from random import randrange
    print(randrange(1, 7))
    nabidka()

def pozdrav():
    jmeno = input("Jak se jmenuješ? ")
    print("Ahoj, ", jmeno, "!")
    nabidka()

nabidka()
