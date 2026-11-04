# Bonus 2 – Metody řetězců
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na heslo a zkontroluj tři věci:
#    je aspoň osm znaků dlouhé, je v něm aspoň jedna číslice
#    a je v něm aspoň jedno velké písmeno.
#
#    Ke každé podmínce vypiš, jestli prošla. Na konec vypiš, jestli
#    je heslo přijaté – to je, jen když prošly všechny tři.
#
#    Na číslici se zeptáš průchodem přes znaky: cyklus for z lekce 3
#    a isdigit() na každý znak.
#    Na velké písmeno stačí porovnat heslo se sebou samým po lower().
#    Jde to ale i cyklem jako u číslice – každého znaku se tam zeptáš
#    metodou isupper().

while True:
    heslo = input("Zadej heslo: ")
    if heslo == heslo.lower():
        print("Zadej alespoň jedno velké písmeno.")
        print("Zkus to znova.")
        continue
    else:
        print("Heslo obsahuje velké písmeno.")
    if len(heslo) < 8:
        delka = False
        print("Heslo je moc krátké")
        print("Zkus to znova.")
        continue
    else:
        if len(heslo) >= 8:
            delka = True
            print("Heslo je dostatečně dlouhé")
    for znak in heslo:
        if znak.isdigit():
            pismeno = True
            print("Heslo obsahuje číslo.")
            break
        else:
            pismeno = False
    if delka == True and pismeno == True:
        print("Tohle je správné heslo.")
        break
    elif delka == False:
        print("Heslo musí mít alespoň 8 znaků.")
        continue
    elif pismeno == False:
        print("Heslo musím mít alespoň jedno číslo.")
        continue
    else:
        print("Někde je chyba.")
        break






