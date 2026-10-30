# def je_heslo_dlouhe(heslo):
#     return len(heslo) > 8

# def zeptej_se_na_jmeno():
#     jmeno = input("Jméno: ")
#     # uprava jmeno
#     return jmeno

# def zeptej_se_na_heslo():
#     return input("Heslo: ")
#     # uprava heslo


# def prihlaseni():
#     jmeno = zeptej_se_na_jmeno()
#     heslo = zeptej_se_na_heslo()
#     if je_heslo_dlouhe(heslo):
#         print("Vítej, ", jmeno)
#     else:
#         print("Heslo nesplňuje délku.")
    

# prihlaseni()

# vek = input("Zadej věk: ")

# print(vek + vek)
# print("Za deset let ti bude", int(vek) + 10)
# print(len(vek))

# if "0" in vek:
#     print("Tvůj věk je kulatý.")
# else:
#     print("Nemáš kulatiny.")

# jmeno = input("Jméno: ")

# for pismeno in jmeno:
#     print(pismeno)

# vek = 30
# jmeno = "Anna"

# print(f"Jsem {jmeno} a je mi {vek}")

# stran_celkem = 320
# kniha = "Malý princ"
# precteno = 183
# print(f"V {kniha} zbývá {stran_celkem - precteno} stránek do konce čtení.")

# def procenta(cast, celek):
#     return cast / celek * 100

# print(f"Máš přečteno {procenta(precteno, stran_celkem):.2f} procent knihy")

# print("Ahoj\n\n\nJani")
# print("Ahoj \"Tomáši\"")
# print("Ahoj \\Tomáši\\")
# print("""Ahoj 


# "Tomáši" """)

# print("pyladies".upper())
# print("Pyladies".lower())
# print("Ahoj Adame".lower().count("a"))

# veta = "Ahoj\nAdame"
# zmensena = veta.lower()
# pocet_n = zmensena.count("n")
# print(pocet_n)
# lepsi_veta = veta.replace("Ahoj", "Dobry den")
# print(lepsi_veta)

# def zeptat_se_na_email():
#     return input("Zadej email: ").lower()

# jmeno = "Dina"
# velke_jmeno = jmeno.upper()
# print(jmeno)
# print(velke_jmeno)

# vek = input("Zadej věk: ")
# if vek.isdigit():
#     print("Za deset let ti bude", int(vek) + 10)
# else:
#     print("Tohle není číslo!")

slovo = "PyLadies"


# for pismeno in slovo:
#     print(pismeno)

print(slovo[0])
print(len(slovo))
print(slovo[len(slovo) - 1]) # poslední pozice je o 1 menší než len()
print(slovo[-1]) # Python umí počítat nazpátek do mínusu od konce
print(slovo[0:2])
print(slovo[-3:]) # od -1 do -3 (bez) do konce
print(slovo[:-3]) # vynechám-li, je to od začátku, nebo od konce
print(slovo[::-1]) # definuju krok (mínus je krok zpátky, podobně jako range)

slovo = "Ahoj"
slovo = slovo[0] + "B" + slovo[1:]
print(slovo)

cena = 100
mesto = "Praha"
teplota = 25.68

print(f"{cena:.2f}")        # 301.29   dvě desetinná místa
print(f"{mesto:12}")        # text na dvanáct míst, zarovnaný doleva
print(f"{teplota:8.1f}")    # číslo na osm míst, zarovnané doprava
print(f"{mesto:>12}")       # > doprava, < doleva
