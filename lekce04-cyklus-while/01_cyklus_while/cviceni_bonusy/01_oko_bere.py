# Bonus 1 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Hra "Oko bere":
#     - Začínáš s 0 body.
#     - V každém kole se ukáže, kolik máš bodů, a zeptáš se,
#       jestli si chceš líznout kartu.
#     - Když ano, počítač ti dá náhodnou kartu 2 až 10
#       (randrange(2, 11)) a přičte ji k bodům.
#     - Cíl je dostat se přesně na 21. Když přetáhneš přes 21, prohráváš.
#     - Když řekneš, že už nechceš, hra skončí a vypíše se výsledek.
#     Nahoru na první řádek nezapomeň:  from random import randrange

from random import randrange
body = 0
while True:
    print("Máš", body, "bodů.")
    liznout = input("Chceš si líznout kartu? (ano/ne) ")
    if liznout == "ano":
        i = randrange(2, 11)
        body = body + i
    elif liznout == "ne":
        break
    if body == 21:
        print("***Vyhráváš***")
        break
    elif body < 21:
        continue
    elif body > 21:
        print("Prohrál jsi :-()")
        break
print("Získal jsi", body, "bodů.")
print("Hra končí.")
