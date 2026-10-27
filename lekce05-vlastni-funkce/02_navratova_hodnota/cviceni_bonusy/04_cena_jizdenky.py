# Bonus 4 – Návratová hodnota
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš funkci cena_jizdenky, která má na vstupu věk cestujícího
#     a základní cenu jízdenky, a vrátí cenu, kterou cestující zaplatí:
#
#       děti do 10 let včetně       zdarma
#       mládež do 18 let včetně     polovina
#       senioři od 65 let včetně    třetina
#       ostatní                     plná cena
#
#     Vyzkoušej ji pro několik věků a ceny vypiš.

def cena_jizdenky(vek, zaklad):
    if vek <= 10:
        return 0
    elif vek <= 18:
        return zaklad / 2
    elif vek >= 65:
        return zaklad / 3
    else:
        return zaklad
    
print("Tvoje jízdenka stojí", cena_jizdenky(15, 30))
print("Tvoje jízdenka stojí", cena_jizdenky(66, 90))
print("Tvoje jízdenka stojí", cena_jizdenky(6, 10))