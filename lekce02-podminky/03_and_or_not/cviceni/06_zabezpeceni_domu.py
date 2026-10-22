# Cvičení 6 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Zabezpečení domu. Dům je zabezpečený, jen když jsou zavřené dveře,
#    zavřená okna a zároveň zapnutý alarm.
#    Zeptej se na všechny tři věci (ano/ne). Pomocí not (…) vypiš
#    "Pozor, dům není zabezpečený!", když zabezpečený NENÍ,
#    jinak vypiš "Zabezpečeno.".

dvere = input("Jsou dveře zavřené (ano/ne)? ")
okna = input("Jsou okna zavřená (ano/ne)? ")
alarm = input("Je alarm zapnutý (ano/ne)? ")

if not (dvere == "ano" and okna == "ano" and alarm == "ano"):
    print("Pozor, dům není zabezpečen.")
else:
    print("Zabezpečen.")
