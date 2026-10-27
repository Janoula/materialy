# Bonus 2 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci zeptej_se_na_heslo(), která se ptá tak dlouho,
#     dokud uživatel nezadá heslo aspoň o 8 znacích, a to heslo vrátí.
#     Uvnitř použij funkci je_heslo_dost_dlouhe z výkladu –
#     zkopíruj si její definici sem nahoru, soubory se navzájem nevidí.

def je_heslo_dost_dlouhe(heslo):
    if len(heslo) >= 8:
        return True
    else:
        return False

def zeptej_se_na_heslo():
    while True:
        heslo = input("Zadej heslo: ")
        if len(heslo) >= 8:
            return heslo
        elif len(heslo) < 8:
            continue
        else:
            return False 

heslo = zeptej_se_na_heslo()
print("Heslo nastaveno na", heslo)