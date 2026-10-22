# Cvičení 4 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Máš proměnnou barva se stavem semaforu ("červená", "oranžová"
#    nebo "zelená"). Vypiš, co má řidič udělat:
#    "červená" → "Stůj", "oranžová" → "Připrav se", "zelená" → "Jeď",
#    cokoli jiného → "Neznámý signál".
barva = input("Jaká svítí barva? ")

if barva == "zelená":
    print("Jeď!")
elif barva == "oranžová":
    print("Připrav se.... ")
elif barva == "červená":
    print("STŮJ")
else:
    print("Signál je neznámý.")
