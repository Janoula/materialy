# Bonus 3 – And, or a not
# Doplň kód pod zadání a soubor spusť (Run).

# Kámen, nůžky, papír. Zeptej se obou hráčů na tah – ať zadají
#     "kamen", "nuzky" nebo "papir". Vypiš, kdo vyhrál:
#       - "Remíza.", když mají oba stejně,
#       - jinak urči vítěze podle pravidel:
#           kámen tupí nůžky, nůžky stříhají papír, papír balí kámen.
#     Vypiš "Vyhrál hráč 1." / "Vyhrál hráč 2.".

volba1 = input("Hráč 1 (kamen/nuzky/papir): ")
volba2 = input("Hráč 2 (kamen/nuzky/papir): ")
if volba1 == volba2:
    print("Remíza.")
elif volba1 == "kamen" and (volba2 == "nuzky" or volba2 != "papir"):
        print("Vyhrál hráč 1.")
elif volba1 == "nuzky" and (volba2 == "papir" or volba2 != "kamen"):
        print("Vyhrál hráč 1.")
elif volba1 == "papir" and (volba2 == "kamen" or volba2 != "nuzky"):
       print("Vyhrál hráč 1.")
else:
      print("Vyhrál hráč 2.")
      