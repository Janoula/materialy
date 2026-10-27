# Cvičení 3 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci vetsi(a, b), která vrátí větší z obou čísel.
#    Funkci max nepoužívej.

def vetsi(a, b):
    if a >= b:
        return a
    else:
        return b

print(vetsi(5, 1))
