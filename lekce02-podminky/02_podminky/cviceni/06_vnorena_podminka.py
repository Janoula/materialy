# Cvičení 6 – Podmínky
# Doplň kód pod zadání a soubor spusť (Run).

# Vnořená podmínka s otázkami na uživatele.
#    Zeptej se: "Máš hlad? (ano/ne)" a ulož odpověď do proměnné hlad.
#    Když má hlad, zeptej se ještě "Máš doma jídlo? (ano/ne)":
#      - když má jídlo, vypiš "Uvař si."
#      - když nemá, vypiš "Objednej si."
#    Když nemá hlad, vypiš "Tak nic, uvidíme později.".

hlad = input("Máš hlad? ")
if hlad == "ano":
    jidlo = input("A máš doma něco k jídlu? ")
    if jidlo == "ano":
        print("Tak si něco uvař.")
    elif jidlo == "ne":
        print("Tak to si něco musíš objednat na Foodoře.")
    else:
        print("Odpovídej prosím jen ano/ne.")
elif hlad != "ne":
    print("Odpovídej prosím jen ano/ne.")
else:
    print("Tak nic, uvidíme se později.")
