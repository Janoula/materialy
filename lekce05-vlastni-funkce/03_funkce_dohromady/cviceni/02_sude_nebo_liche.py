# Cvičení 2 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Napiš dvě funkce:
#    je_sude(cislo) vrátí True, nebo False,
#    popis(cislo) vrátí text "4 je sudé" nebo "7 je liché" a uvnitř
#    se na je_sude zeptá.
#    Pak v cyklu for vypiš popis čísel od 1 do 6.

def je_sude(cislo):
    if cislo % 2 == 0:
        return True
    else:
        return False

def popis(cislo):
    if je_sude(cislo) == True:
        return print(cislo, "je sudé")
    else:
        return print(cislo, "je liché")

for cislo in range(1,15):
    popis(cislo)
