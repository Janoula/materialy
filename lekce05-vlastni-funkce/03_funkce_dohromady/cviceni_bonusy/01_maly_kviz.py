# Bonus 1 – Funkce dohromady
# Doplň kód pod zadání a soubor spusť (Run).

# Malý kvíz. Napiš funkci otazka(text, spravna_odpoved), která
#     otázku položí, odpověď načte a vrátí True, když je správná.
#     Polož tři otázky, počítej správné odpovědi a nakonec vypiš skóre.


def otazka(text, spravna_odpoved):
    answer = input(text)
    return answer == spravna_odpoved

skore = 0
if otazka("Kolik nohou má ještěrka? ", "4"):
    skore = skore + 1
if otazka("Jak se jmenuje současný prezident ČR? ", "Petr Pavel"):
    skore = skore + 1
if otazka("Hlavní město Francie? ", "Paříž"):
    skore = skore + 1

print("Tvoje skóre je", skore, "bodů.")

