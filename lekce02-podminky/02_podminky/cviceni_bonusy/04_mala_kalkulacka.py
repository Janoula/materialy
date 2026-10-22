2
# Doplň kód pod zadání a soubor spusť (Run).

# Malá kalkulačka.
#     Zeptej se na dvě čísla a na znaménko (+, -, *, /).
#     Podle znaménka vypiš výsledek správné operace.
#     Bonus v bonusu: ošetři dělení nulou vlastní hláškou.

         

prvni_cislo = float(input("Zadej první číslo: "))
operace = input("Zadej operaci (+, -, *, /): ")
druhe_cislo = float(input("Zadej druhé číslo: "))

if operace == "+":
    print(prvni_cislo + druhe_cislo)
elif operace == "-":
    print(prvni_cislo - druhe_cislo)
elif operace == "*":
    print(prvni_cislo * druhe_cislo)
elif operace == "/":
    if druhe_cislo == 0:
        print("Nulou nedělím!")
    else:
        print(prvni_cislo / druhe_cislo)



