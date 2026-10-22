# Bonus 5 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Palindrom. Uživatel zadá slovo. Zjisti, jestli se čte stejně
#     zepředu i zezadu (třeba "kajak" nebo "radar").
#     Zamysli se, jak si slovo poskládáš pozpátku a jak obě verze porovnáš.

slovo = input("Slovo: ")
druhe = ""
for i in slovo:
    druhe = i + druhe
if slovo == druhe:
        print("Palindrom.")
else:
    print("Není to palindrom.")
