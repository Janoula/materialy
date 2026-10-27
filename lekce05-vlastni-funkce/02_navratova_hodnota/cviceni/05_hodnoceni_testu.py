# Cvičení 5 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci hodnoceni(body), která vrátí "prošla" pro 50 a víc bodů
#    a "neprošla" pro méně. Pak se v cyklu while ptej na body tak dlouho,
#    dokud uživatel nezadá -1, a u každého zadání vypiš hodnocení.

def hodnoceni(body):
    if body >= 50:
        return print("prošla")
    else:
        return print("neprošla")


while True:
    body = int(input("Kolik máš bodů? (-1 = konec)"))
    if body == -1:
        break
    hodnoceni(body)
print("konec")

