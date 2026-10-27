# Cvičení 3 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci soucet_do(n), která vrátí součet čísel od 1 do n.
#    soucet_do(5) vrátí 15.

def soucet_do(n):
    soucet = 0
    for cislo in range(1, n + 1):
        soucet = soucet + cislo
    return soucet

print("Součet je:", soucet_do(5))

print("Součet je:", soucet_do(10))
