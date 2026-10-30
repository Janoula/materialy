# Bonus 1 – Skládání textu
# Doplň kód pod zadání a soubor spusť (Run).

# Vypiš diplom v rámečku z hvězdiček:
#
#    **************************
#    * Anna Nováková          *
#    * Python pro začátečnice *
#    **************************
#
#    Rámeček musí být přesně tak široký, jak je potřeba. Když jméno
#    nebo název kurzu vyměníš za delší, musí se přizpůsobit sám –
#    šířku tedy spočítej, nepiš ji natvrdo.

jmeno = input("Jméno: ")
kurz = input("Název kurzu: ")
znak = input("Zadej znak */=/-/.")
delka_textu = int(max(len(jmeno), len(kurz)))

delka_ramecku = delka_textu + 4
print(delka_ramecku * znak)
print(f"{znak} {jmeno:{delka_textu}} {znak}")
print(f"{znak} {kurz:{delka_textu}} {znak}")
print(delka_ramecku * znak)

