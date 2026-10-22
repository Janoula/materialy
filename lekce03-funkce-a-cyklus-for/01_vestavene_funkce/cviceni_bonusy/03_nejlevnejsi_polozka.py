# Bonus 3 – Vestavěné funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Cíl a rozpočet. Uživatel zadá cenu tří položek. Vypiš nejlevnější
#     a nejdražší z nich a jestli se všechny tři vejdou do rozpočtu 1000 Kč.

jidlo = int(input("Jidlo: "))
cestovne = int(input("Cestovne: "))
zabava = int(input("Zabava: "))
print(min(jidlo, cestovne, zabava))
print(max(jidlo, cestovne, zabava))

cena = jidlo + cestovne + zabava
if cena <= 1001:
    print("vejde se do rozpočtu")
else:
    print("je to moc drahé")