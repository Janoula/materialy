# Cvičení 1 – Měnění seznamů
# Doplň kód pod zadání a soubor spusť (Run).

# Spravuješ playlist na večírek. Postupně:
#    - první skladbu přesuň na konec,
#    - na druhé místo vlož přání "Jožin z bažin",
#    - odeber skladbu "Holky z naší školky",
#    - vypiš playlist.
#
#    Vyjít má:  ['Severní vítr', 'Jožin z bažin', 'Trezor']

playlist = ["Trezor", "Severní vítr", "Holky z naší školky"]

prvni = playlist.pop(0)
print(playlist)
playlist = playlist + [prvni]
print(playlist)
playlist[1:1] = ["Jožin z bažin"]
print(playlist)
playlist.remove("Holky z naší školky")
print(playlist)
