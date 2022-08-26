# 3.9 For SIKLI

mehmonlar = ["Ali", "Vali", "Anvar", "Sarvar"]
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}\n"
          f"Sizni 17-sentabr uuni tug'ilgan kunimga taklif qilaman.\n")
print("Hurmat bilan Odilbek\n")

cars = ["nexia", 'tico', 'damas']
for car in cars:
    print(f"{car.title()} ko'rganlar qilar havas\n")

cars = ["nexia", 'tico', 'damas']
for car in cars:
    print(car.title())
print("Ko'rganlar qilar havas!\n")

# For siklini sonlarda ishlatib ko'ramiz

sonlar = list(range(1, 12))
for son in sonlar:
    print(f"{son}  ning kvadrati {son**2} ga teng")

sonlar = list(range(1, 10))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
print(sonlar)
print(sonlar_kvadrati)

yulduzlar = list(range(1, 21))
yulduzlar_k = []
for yulduz in yulduzlar:
    yulduzlar_k.append("*")
    print(yulduzlar_k)


# Input va for
#dostlar = []
#print("5 ta eng yaqin do'stingizni kiritiing.")
#for n in range(5):
#    dostlar.append(input(f"{n+1} Ismini kiriting.\n>>>"))
#print(dostlar)

#Amaliyot

mehmonlar = ["Ali", "Vali", "Anvar", "Sarvar"]
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}\n"
          f"Sizni 17-sentabr uuni tug'ilgan kunimga taklif qilaman.\n")
print("Kod 4 marta takrorlandi.\n")

juft_son = list(range(0, 20, 2))
print('Juft son:')
for json in juft_son:
    print(json)
toq_son = list(range(1, 20, 2))
print('Toq son:')
for tson in toq_son:
    print(tson)

kinolar = []
print("5 ta eng sevimli kinongiz nomini kiriting.")
for r in range(5):
    kinolar.append(input(f"{r+1}-kino nomini kiriting.\n>>>"))
for kino in kinolar:
    print(f"Sevimli kinoyingiz: {kino}")


odamlar = []
son = int(input('Bugun necha kishi bilan suhbatlashdingiz'))
for i in range(son):
    odamlar.append(input(f"Ularni sanab bering.\n>>>"))
for odam in odamlar:
    print(f"Siz bugun {odam} bilan uchrashgansiz.")
