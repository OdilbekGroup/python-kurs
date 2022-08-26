# # 4.2 if-else operatori

son = int(input("Biror son kiriting.\n>>>"))
if son > 0:
    print(f"{son} - musbat son")
else:
    print(f"{son} - manfiy son")


yosh = int(input(f"Yoshingizni kiriting."))
if yosh<=7:
    print('Sizga avtobus bepul!')
else:
    print('Chipta narxi 5 000 so.m')

# Bir qator if-else
yosh = int(input('Yoshingiz nechada?'))
if yosh > 65: print('Siz covid-10 risk guruhida ekkansiz.')

x, y = 25, 50
print('x>y') if x>y else print('x<y')

# # Amaliyot
# #1.!
avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())

# #1.2
javob = float(input("12x6 necha bo'ladi?\n>>>"))
if javob!=72:
    print("Javob noto'g'ri")
else:
    print("Javob to'g'ri")

# #1.3
ypsh = int(input('Yoshingiz nechada?\n>>>'))
if ypsh>18:
    print('Xush kelibsiz!')
else:
    print('Kirish mumkin emas.')

# #1.4
yil = int(input("Nechanchi yil tug'ilgansiz?\n>>>"))
if 2022 - yil<18:
    print(f"Yoshingiz {2022-yil} da ekan.")
    print('kirish mumkin emas.')
else:
    print("Xush kelibsiz!")
# #1.5
login = (input("Login kiriting."))
if len(login)<=5:
    print("Login kamida 5 ta belgidan iborat bo'lishi kerak.")
else:
    print("Login qabul qilindi.")


# #2.1
cars = ['Tayota', "mazda", 'hyundai', 'gm', 'kia']
for car in cars:
    if car=="gm":
        print(car.upper())
    else:
        print(car.title())

# #3
cars = ['Tayota', "mazda", 'hyundai', 'gm', 'kia']
for car in cars:
    if car!="gm":
        print(car.upper())
    else:
        print(car.title())

# #4
login = input("Loginingiz kiriting.")
if login.lower() == "admin":
    print("Xush kelibsiz, admin! "
          "Foydalanuvchilar ro'yhatini ko'rasizmi? ")
else:
    print(f'Xush kelibsiz, {login}')

# #5
print('Ikki ta son kiriting.')
son1 = int(input("birinchi son\n>>>"))
son2 = int(input("Ikkinchi son\n>>>"))
if son1 == son2:
    print(f"{son1} va {son2} teng")
else:
    print(f"{son1} va {son2} teng emas")

# #6
son = int(input("Ixtiyoriy son kiriting."))
if son > 0:
    print(f"{son} musbat son")
else:
    print(f"{son} manfiy son")



son = int(input("Musbat son kiriting."))
if son >0:
    print(f"{son} ning ildizi {int(son**(1/2))}")
else:
    print(f"Iltimos, musbat son kiriting.")

inputNumber = int(input('Biror sonni kiriting.'))
juftTow_son = inputNumber % 2
if juftTow_son==0:
    print(f"{inputNumber} - juft son")
else:
    print(f"{inputNumber} - toq son")
