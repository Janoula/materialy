# Bonus 4 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Teplotní skok. Uživatel postupně zadá sedm denních teplot
#     (klidně i záporných). Najdi a vypiš největší skok mezi dvěma
#     sousedními dny – tedy největší rozdíl teplot ze dne na den
#     (bez ohledu na to, jestli teplota stoupla, nebo klesla).

akt_skok = 0
prvni = int(input("Teplota: "))
for i in range(6):
    t = int(input("Teplota: "))
    skok = abs(t - prvni)
    if akt_skok > skok:
        akt_skok = skok
    prvni = t
print("Největší skok:", skok)

