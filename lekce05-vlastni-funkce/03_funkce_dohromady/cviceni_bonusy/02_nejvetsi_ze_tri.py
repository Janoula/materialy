# Bonus 2 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci nejvetsi_ze_tri(a, b, c), která vrátí největší
#     ze tří čísel. Uvnitř použij funkci vetsi(a, b) z minulé složky –
#     zkopíruj si její definici sem nahoru, soubory se navzájem nevidí.

def vetsi(a, b):
    if a >= b:
        return a
    else:
        return b

def nejvetsi_ze_tri(a, b, c):
    if c >= vetsi(a, b):
        return c
    else:
        return vetsi(a, b)

print(nejvetsi_ze_tri(15, -1, 3))