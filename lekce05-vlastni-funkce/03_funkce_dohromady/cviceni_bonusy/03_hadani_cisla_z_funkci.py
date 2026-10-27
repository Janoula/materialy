# Bonus 3 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Hra na hádání čísla, celá poskládaná z funkcí – losování,
#     načtení tipu i vyhodnocení ať má každé svoji.
#     Hlavní cyklus while pak jenom tyhle funkce volá.

def losovani():
    from random import randrange
    return randrange(1, 7)
   
def nacteni():
    return int(input("Tvůj tip: "))
    
    
def vyhodnoceni(tip, los):
    return tip == los

los = losovani()
while True:
    tip = nacteni()
    if vyhodnoceni(tip, los):
        print("Správně!")
        break
    else:
        print("Tak příště...")
