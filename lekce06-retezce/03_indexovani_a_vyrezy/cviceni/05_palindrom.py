# Cvičení 5 – Indexování a výřezy
# Doplň kód pod zadání a soubor spusť (Run).

# Zeptej se na slovo a vypiš, jestli se čte stejně zepředu i pozpátku.
#    Na velikosti písmen ať nezáleží, takže "Oko" projde taky.

slovo = input("Slovo: ").strip().lower()
palindrom = slovo[::-1]
if slovo.lower() == palindrom.lower():
    print("Čte se z obou stran stejně.")
else:
    print("Není to palindrom.")
