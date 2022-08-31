# 5.2 Lug'at bilan ishlash

car = {
    'model':'Ferrari',
    'color':'qizil'
}
print(car['model'])
print(car['color'] + '\n')

student = {
    'name': 'Murod Olimov',
    'yearOfBirth': 2000,
    'age':22
}

print(f"talaba: {student['name']}\n"
      f"Tug'ilgan yili: {student['yearOfBirth']}-yil\n"
      f"Yoshi: {student['age']}\n")

student['course'] = 4
student['facultet'] = 'Informatika'

print(student)

car = {}
car['model'] = 'Nexia 3'
car['position'] = 2
car['color'] = 'oq'
car['price'] = 33000

print(f"Model: {car['model']}\n"
      f"Pozitsiya: {car['position']}\n"
      f"Rangi: {car['color']}\n"
      f"")

#  Qiy,atni o'zgartirish

car['price'] = 30000
print(f"{car['color']} - {car['model']}, {car['price']}$\n")

# Kalit so'z va qiymat juftligini o'chirish
print(car)
del car['color']
print(car)

# Amaliyot
father = {
    'firstName': 'Rustam',
    "lastName": "DJumamuratov",
    'yearOfBirth': 1981
}
mother = {
    'firstName': 'Yulduz',
    "lastName": "Muratova",
    'yearOfBirth': 1982
}
sister = {
    'firstName': 'Sevinchoy',
    "lastName": "Xudaybergenova",
    'yearOfBirth': 2013
}

food = {
    'firstFood':'Manti',
    'secondFood':'Chuchvara',
    'thirdFood':'Besh barmoq',
    'fourthFood':"kartoshka bo'rak",
    'fifthFood':"tuxum bo'rak",
}
print(f"\nDadam {food['secondFood'].lower()}ni yoqtiradi.\n"
      f"Onam {food['firstFood'].lower()}ni yoqtiradi.\n"
      f"Singlim va men {food['fourthFood']}ni yoqtiramiz.")

# Lug'at elementlari bilan ishlash

car = {
    'model':'Lacwtti',
    'color':'oq',
    'position':2
}
print(car.items())

for kalit, qiymat in car.items():
    print(f"{kalit}: {qiymat}\n")

# Endi faqat kalitlarni olib ko'ramiz.

products = {
    'Olma':10000,
    'Anor':15000,
    'Behi':18000,
    'Uzum':16000,
}
print("Do'kondagi mahsulotlar")
for k, q in products.items():
    print(k)

buy = ["Olma", "Anor", "Behi", "Uzum"]
for n in products:
    if n in buy:
        print(f"{n.title()} - {products[n]} so'm")

for think in buy:
    if think not in products:
         print(f"Kechirasiz, bizda {think} yo'q")

print("Do'konimizdagi mahsulotlar:")
for product in sorted(products):
    print(product)

telefonlar = {
    'Ali':'Iphone 13 pro',
    'Vali':'Samsung Galaxy J2',
    'Anvar':'vivo Y15',
}

print(telefonlar.values())

print("\nFoydalanuvchilarning telefonlari:")
for tel in telefonlar.values():
    print(tel)

telefonlar = {
    'Ali':'Iphone 13 pro',
    'Vali':'Samsung Galaxy J2',
    'Anvar':'vivo Y15',
    'Sarvar':'Iphone 13 pro',
    'Komil':'Samsung Galaxy J2',
    'Asqar':'vivo Y15',
    'Orif':'Iphone 13 pro',
    'Daston':'Samsung Galaxy J2',
    'Mardon':'vivo Y15',
}

print("\nFoydalanuvchilarning telefonlari:")
for tel in telefonlar.values():
    print(tel)

print("\nFoydalanuvchilarning telefonlari:")
for tel in set(telefonlar.values()):
    print(tel)

# AMALIYOT

dictionaryPython = {
    'print': "Konsolga matn chiqarish",
    'for': 'Takrorlash sikili',
    'if': "Agarda shart operatori",
    'else': "Aks holda shart operatori",
    'boolean': "Mantiqiy amallar ma'lumot turi",
    'float': "butun sonlar ma'lumot turi",
    'string': "matnli ma'lumot turi",
    'title': "so'zning bosh harfini katta qiluvchi metod",
    'lower': "So'zning barcha harflarini kichik qiluvchi metod",
    'upper': "So'zdagi barcha harflarni katta qilib beradi."
}
for key, value in sorted(dictionaryPython.items()):
    print(f"\n{key}: {value}")

state_Capital = {
    "O'zbekiston":"Toshkent",
    "Qozog'iston":"Astana",
    "Ozarbayjon":"Boku",
    "Ukraina":"Kiev",
    "Rossiya":"Moskva"
}

inputState = input("Davlat nomini kiriting.")
for state in state_Capital:
    if inputState in state:
        print(f"{inputState}ning poytaxti {state_Capital[state]}")

