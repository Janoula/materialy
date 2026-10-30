# Bonus 1 – Metody řetězců
# Doplň kód pod zadání a soubor spusť (Run).

# Tři jména přišla z formuláře rozbitá – mezery na krajích a náhodná
#    velikost písmen. U každého vypiš jeden řádek: uklizené jméno
#    a k němu přihlašovací jméno, které z něj vyrobíš. To je celé
#    malými písmeny a místo mezery má tečku.
#
#    Pro "  anna NOVÁKOVÁ  " má vyjít:
#    Anna Nováková -> anna.nováková

jmeno1 = "  anna NOVÁKOVÁ  "
jmeno2 = "PETRA svobodová"
jmeno3 = " tereza Dvořáková   "

print(f"{jmeno1.strip().title()} -> {jmeno1.strip().lower().replace(" ",".")}")
print(f"{jmeno2.strip().title()} -> {jmeno2.strip().lower().replace(" ",".")}")
print(f"{jmeno3.strip().title()} -> {jmeno3.strip().lower().replace(" ",".")}")
