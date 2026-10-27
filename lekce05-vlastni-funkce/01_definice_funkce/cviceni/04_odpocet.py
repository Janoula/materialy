# Cvičení 4 – Definice funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci odpocet(od), která odpočítá od zadaného čísla
#    dolů k 1 a nakonec vypíše "Teď!".
#    Zavolej ji pro 3 a pro 5.
#    Krok v range jde nastavit i tak, aby se počítalo dolů.

def odpocet(cislo):
    for krok in range(1, cislo + 2):
        print(cislo)
        cislo = cislo - 1
        if cislo == 0:
            break
        else:
            continue
    print("Teď!")

odpocet(3)
