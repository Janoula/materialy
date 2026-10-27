# def vypis_cisla_do_max_hodnota(max_hodnota, jmeno_volani, ukaz_caru = True):
#     for aktualni_cislo in range(1, max_hodnota + 1):
#         print(jmeno_volani+":", aktualni_cislo)
#     if ukaz_caru:
#         print("-" * 30)

# vypis_cisla_do_max_hodnota(1, "Volání A")
# vypis_cisla_do_max_hodnota(10, "Volání B")
# vypis_cisla_do_max_hodnota(20, "Volání C", False)

def cena_mhd(vek):
    print("Pocitam cenu listku pro", vek)
    if vek < 6:
        return 0
    elif vek < 18:
        return 39
    elif vek < 65:
        return 50
    else:
        return 0
zustatek_uctu = int(input("Kolik máš v peněžence? "))
roky = int(input("Kolik máš roků? "))
cena_jizdenky = cena_mhd(roky)
print("Cena jízdenky je:", cena_jizdenky)
zustatek_uctu = zustatek_uctu - cena_jizdenky
print("Zůstatek v peněžence je", zustatek_uctu)


