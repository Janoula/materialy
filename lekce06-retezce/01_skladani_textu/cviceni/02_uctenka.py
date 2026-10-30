# Cvičení 2 – Skládání textu
# Doplň kód pod zadání a soubor spusť (Run).

# Vypiš účtenku tak, aby ceny byly pod sebou: název zarovnaný doleva
#    na dvanáct míst, cenu doprava na osm míst se dvěma desetinnými
#    místy. Na konec přidej řádek se součtem.
#
#    Když je součet vyšší než 150 Kč, přidej ještě řádek se slevou
#    deset procent a řádek s cenou po slevě.

polozka1 = "káva"
cena1 = 39
polozka2 = "dort"
cena2 = 84.5
polozka3 = "čaj"
cena3 = 15

print(f"{polozka1:<12}{cena1:>8.2f}\n{polozka2:<12}{cena2:>8.2f}\n{polozka3:<12}{cena3:>8.2f}")
soucet = cena1 + cena2 + cena3
print(f"Celkem {soucet} Kč.")
if soucet > 150:
    print(f"Sleva 10% činí {soucet / 10} Kč")
    print(f"Konečná cena je {soucet * 0.9} Kč po slevě")
else:
    print(f"Konečná cena je {soucet} Kč.")
