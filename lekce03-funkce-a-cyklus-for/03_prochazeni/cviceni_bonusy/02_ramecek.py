# Bonus 2 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Rámeček. Uživatel zadá velikost N. Vnořenými cykly nakresli
#     čtverec N x N, kde okraj tvoří X a vnitřek je prázdný. Pro N=4:
#         X X X X
#         X     X
#         X     X
#         X X X X
#     Zamysli se: na kterém řádku a sloupci se kreslí X a kdy mezera?

a = int(input("Velikost: "))
for i in range(1, a + 1):
    for j in range(1, a + 1):
        if i == 1 or i == a or j == 1 or j == a:
            print("X", end=" ")
        else:
            print(" ", end=" ")
    print()

