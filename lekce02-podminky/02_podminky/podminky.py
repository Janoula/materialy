# vek = int(input("Kolik je ti let? "))

#if vek >= 18:
#    print("Můžeš volit.")
#    print("Jsi plnoletá.")

# ukončit interaktivní Python Ctrl + Z

#teplota = 18
#if teplota > 15:
#    print("To je pěkně.")
#else:
#    print("Vezmi si bundu.")

#znamka = 1
#if znamka == 1:
#    print("Výborně. ")
#elif znamka == 2:
#    print("Chvalitebně. ")
#else:
#    print("Příště to už ani nebudu opravovat.")

#venku_prsi = False
#mam_destnik = False

#if venku_prsi:
 #   if mam_destnik:
  #      print("Co se dá dělat... ale nezmoknu!")
   # else:
    #    print("Nejsem z cukru.")
#else:
 #   if mam_destnik:
  #      print("Táhnu ten deštník zbytečně.")
   # else:
    #    print("Mám štěstí, že neprší, když zrovna nemám deštník.")

a = -1
b = 5

print(not (a > 0 and b > 0))
print(a < 0 or b < 0)

print("not True je", not True)
print("not False je", not False)

a = int(input("Zadej stranu a "))
b = int(input("Zadej stranu b "))
if a > 0 and b > 0:
    if a == b:
        print("Tohle je čtverec.")
    print("Obsah je", a * b)
else:
    print("Tohle není obdélník.")


# vek = 5
# print(vek >= 18 and vek < 65)

# den = input("Co je za den? ")
# if den == "sobota" or den == "neděle":
#     print("Je víkend.")
# #else:
#     print("Musíme do práce.")