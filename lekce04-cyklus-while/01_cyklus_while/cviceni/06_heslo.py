# Cvičení 6 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Ptej se na heslo. Když uživatel zadá "pyladies", vypiš "Vítej!"
#    a skonči. Když se splete třikrát, vypiš "Zablokováno." a skonči taky.
#    Z cyklu se v obou případech dostaneš příkazem break.

pokus = 0

while True:
    heslo = input("Zadej heslo: ")
    pokus = pokus + 1
    if heslo == "pyladies":
        print("Vítej.")
        break
    if pokus == 3:
        print("Zablokovano.")
        break
    print("Špatně. Zkus to znovu.")
        
    

