# 3.6 Ro'yhatalr - Lists

mevalar = ["Olma", "O'rik", "Anjir"]
narxlar = [12000, 10900, 11000]
numbers = ["bir", "ikki", 3, 4, 5] # aralash ro'yhat
fikrlar = [] # bo'sh ro'yhat

# ro'yhat elementlari
# indeks bilan chaqirish
print('birinchi meva ' + mevalar[0].lower())
print('Ikkinchi meva ' + mevalar[1].lower())
print('Oxirgi meva ' + mevalar[2].lower())

# Uzun ro'yhatdan oxirgi elementni olish
sonlar = [5, 4, 3, 2, 1, 0, -1,  -2, -3, -4, -5]
print(sonlar[-1])

# Ro'yhat elementlarini o'zgartirish
print(f"Oldingi narxlar {narxlar}")
narxlar[0] = 13000
narxlar[1] = 11000
narxlar[2] = 10000
print(f"Yangi  narxlar {narxlar}")

# Mavjud bo'lmagan indeexga qiymat yuklab bo'lmaydi.
# narxlar[4] = 14555
# print(narxlar[4])

# Ro'yhatga yangi element qo'shish
users = ["Odilbek", "G'ayrat", "Diyorbek", "Suhrob"]
users.append("Daston")
print(users)

# Bo'sh ro'yhatni to'ldirish
cars = []
cars.append("Spark")
cars.append("Nexia 3")
cars.append("Tico")
print("To'ldirilgan ro'yhat ", cars)

# Ro'yhatning istalgan qismiga element qo'shish
cars = ["Nexia", 'Cobalt', "Damas"]
print(cars)
cars.insert(0, "Malibu")
cars.insert(3, "Spark")
print(cars)

# Ro'yhatdan element o'chirish
mevalar = ["Anjir", "Shaftoli", "O'rik", "Olma"]
print(mevalar)
del mevalar[1]
print(mevalar)

# O'chirishning boshqa usul
mevalar.remove("Anjir")
print(mevalar)

# .remove metodi ro'yhatda takrorlangan qiymatlar bo'ladigan bo'lsa
# va ularni o'chirish topshirilsa ulardan eng birinchisini o'chiradi
mevalar.append("Olma")
mevalar.append("Olma")
print(mevalar)
mevalar.remove("Olma")
print(mevalar)
mevalar.remove("Olma")
mevalar.remove("Olma")
print(mevalar)

# Bir ro'yhatdagi elementni sug'urib olib boshqasiga qo'shish
mahsulotlar = ["Go'sht", "Yog'", "Sut", "Qatiq"]
bozorlik = mahsulotlar.pop(2)
print(f"Men {bozorlik} oldim")
print(f"Qolgan mahsulotlar: {mahsulotlar}\n")

# AMALIYOT
ismlar = ["Diyorbek", "G'ayrat", "Daston"]
print(f"{ismlar[0]} ahvollar qanday?")
print(f"{ismlar[1]} ahvollar qanday?")
print(f"{ismlar[2]} ahvollar qanday?\n")

t_shaxslar = ["Amir Temur", "Alisher Navoiy", "Zahiriddin Muhammad Bobur"]
z_shaxslar = ["Anvar Narzullayev", "Muhammad Ali", "Stiv Jobs"]
print(t_shaxslar)
print(z_shaxslar)
suhbat = t_shaxslar.pop(1)
suhbat1 = z_shaxslar.pop(2)
print(f"\nMen tarixiy shaxslardan {suhbat} bilan ommaviy \nshaxslardan esa {suhbat1} bilan suhbat qilishni hohlar edim.")

friends = []
friends.append("Diyorbek")
friends.append("G'ayrat")
friends.append("Daston")
friends.append("Suhrob")
friends.append("Odilbek")
friends.append("Odilbek")
print(friends)
friends.remove("Odilbek")
print(friends)
friends.insert(0, "Jaloliddin")
friends.insert(4, "Inomjon")
friends.insert(-1, "Javohir")
print(friends)
