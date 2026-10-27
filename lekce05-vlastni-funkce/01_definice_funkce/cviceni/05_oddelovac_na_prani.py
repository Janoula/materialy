# Cvičení 5 – Definice funkce
# Doplň kód pod zadání a soubor spusť (Run).

# Předělej oddělovač z prvního úkolu tak, aby šlo při volání vybrat
#    znak a délku řádku. Když se nevybere nic, ať vypíše 30 hvězdiček
#    jako dřív.
#    Funkce musí zvládnout všechna tři volání:
#        oddelovac()
#        oddelovac("=")
#        oddelovac("-", 10)

def oddelovac(znak = "*", pocet = 30):
    print(znak * pocet)

oddelovac()
oddelovac("=")
oddelovac("-", 15)

# def oddelovac(znak = True, pocet = True):
#     if znak == "=":
#         print("=" * pocet)
#     elif znak == "-":
#         print("-" * pocet)
#     else:
#        print("*" * 30)

# oddelovac()
# oddelovac("=")
# oddelovac("-", 10)
