# Cvičení 2 – Procházení textu
# Doplň kód pod zadání a soubor spusť (Run).

# Bum-Bác. Tuhle úlohu znáš z minula pro jedno číslo – teď ji necháme
#    proběhnout cyklem. Vypiš čísla od 1 do 30, ale:
#    - za dělitelné třemi i pěti zároveň vypiš "BumBác",
#    - za dělitelné jen třemi vypiš "Bum",
#    - za dělitelné jen pěti vypiš "Bác",
#    - jinak vypiš samotné číslo.

for i in range(1,31):
    if i % 3 == 0 and i % 5 == 0:
        print("Bumbác")
    elif i % 3 == 0:
        print("Bum")
    elif i % 5 == 0:
        print("Bác")
    else:
        print(i)
print("hotovo")
