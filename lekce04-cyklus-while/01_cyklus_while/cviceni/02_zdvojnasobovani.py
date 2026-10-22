# Cvičení 2 – Cyklus while
# Doplň kód pod zadání a soubor spusť (Run).

# Začni s číslem 1 a v cyklu ho pořád zdvojnásobuj. Zastav se,
#    jakmile přesáhne 1000, a vypiš, kolikrát jsi ho zdvojnásobila.

treshold = int(input("Kdy se zastavím? "))
cyklus = 0
a = 1
while a <= treshold:
    a = a * 2
    cyklus = cyklus + 1
print("Číslo, které přesáhlo:", a)
print("Počet zdvojnásobení do", treshold, "je", cyklus, ".")
