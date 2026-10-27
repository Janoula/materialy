# Bonus 1 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci zkontroluj_pin(spravny_pin), která dá uživateli
#     tři pokusy zadat PIN. Když se trefí, vrátí True, jinak False.
#     Po zavolání vypiš "Odemčeno." nebo "Karta zablokována.".

def zkontroluj_pin(spravny_pin):
    pokus = 0
    while pokus < 3:
        zadej = input("Zadej PIN: (tři pokusy)")
        pokus = pokus + 1
        if zadej == spravny_pin:
            return print("Odemčeno")
        elif pokus < 3:
            continue
        else:
            return print("Karta zablokována.")
    print("Pokusy vyčerpány.")

zkontroluj_pin("1234")