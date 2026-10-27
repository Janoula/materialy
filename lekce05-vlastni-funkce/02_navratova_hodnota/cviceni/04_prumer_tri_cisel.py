# Cvičení 4 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci prumer(a, b, c), která vrátí průměr tří čísel
#    zaokrouhlený na jedno desetinné místo.

def prumer(a, b, c):
    return round(((a + b + c)/3), 1)

print(prumer(1, 5, 80))
