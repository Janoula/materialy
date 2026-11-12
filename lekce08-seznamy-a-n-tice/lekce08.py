hoste = ["Marta", "Shrek", "Petr Pavel"]
print(hoste)

organizator = "Gábinka"
organizator = organizator.upper() + " von Little Stars of Space"
print(organizator)
hoste = hoste + ["Karkulka"]
# print(organizator, "zve", hoste, "na vánoční večírek.")
# print(organizator)
# print("Na večírek je pozváno:", len(hoste), "hostů.")

pocet_hostu = len(hoste)
pozvanka = "Zvu Vás na vánoční večírek. " + organizator[0] + organizator[6]
print(pozvanka)

for host in range(pocet_hostu):
        print("Zveme Vás,", hoste[host])

# print("První pozvánku dostal/a:", hoste[0])

blacklist = ["Anička Dajdou", "vlk"]
prichozi = input("Jak se jmenuješ? ")

def kontrola(prichozi, hoste, blacklist):
    if prichozi in hoste:
        print("Pojď dál", prichozi)
    elif prichozi in blacklist:
        print("Rychle se ztrať, než si tě všimne Karel.")
    else:
        print("Nejsi zván.")
    

kontrola(prichozi, hoste, blacklist)

def pozvi(jmeno, hoste):
     hoste.append(jmeno)

pozvi("Vojta", hoste)
# print(hoste)
hoste[5:6] = ["Tom", "Vojta"]
# print(hoste)
hoste[0] = "Martina"
# print(hoste)

#pop, join, split, append, remove

print(organizator.split())
inicialy = organizator.split()[0][0] + organizator.split()[1][0]

inicialy = []
for slovo in organizator.split():
    inicialy.append(slovo[0])
print("-".join(inicialy))
print(inicialy)

def ban(jmeno, hoste):
      hoste.remove(jmeno)

ban("Shrek", hoste)
print(hoste)
hoste.pop(0)

fronta = ["Vojta,", "vlk", "Petra", "Oslik", "Shrek"]
print(fronta)
kontrola(fronta.pop(0), hoste, blacklist)
print(fronta)

# for host in hoste:
#         if prichozi == host:
#                 print("Pojď dál", prichozi)