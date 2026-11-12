# Cvičení 3 – Debugger
# Spusť soubor (Run) třikrát a zadej postupně hesla ze seznamu níž.
# Chyby jsou dvě. Najdi je debuggerem a oprav.

# 1. chybba ř. 16 - upper na lower()
# 2. chyba po ř. 22 chybí break - správně ma_cislici = True se dalsim znakem, který není digit přepíše na False.
# Kontrolu hesla znáš z bonusu v šesté lekci. Heslo projde, když má
# aspoň osm znaků, aspoň jednu číslici a aspoň jedno velké písmeno.
#
#   - Pyladies2026 – má projít
#   - 2026Pyladies – má projít
#   - pyladies2026 – nemá projít, chybí v něm velké písmeno

heslo = input("Zadej heslo: ")

dost_dlouhe = len(heslo) >= 8
ma_velke = heslo != heslo.lower()

ma_cislici = False
for znak in heslo:
    if znak.isdigit():
        ma_cislici = True
        break
    else:
        ma_cislici = False

print(f"Aspoň osm znaků:  {dost_dlouhe}")
print(f"Obsahuje číslici: {ma_cislici}")
print(f"Velké písmeno:    {ma_velke}")

if dost_dlouhe and ma_cislici and ma_velke:
    print("Heslo přijato.")
else:
    print("Heslo nevyhovuje.")
