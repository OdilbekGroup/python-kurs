# 4.4 And va or operatorlari

# inputDay = input('Bugun qaysi kun?')
# if inputDay.lower() == "shanba" or inputDay.lower() == 'yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print('Bugun ish kuni')
#
# print(True or True)
# print(False or True)
# print(True or False)
# print(False or False)

# inputDay = input("Bugun qaysi kun?")
# inputTemprsature = int(input("Bugun harorat qanday?"))
# if inputDay.lower() == "shanba" and inputTemprsature >30:
#     print("Cho'milishga ketdik")
# elif inputDay.lower()=='yakshanba' and inputTemprsature<30:
#     print("Bugun uyda dam olamiz")
# else:
#     print("Bugun ishlar ekanmiz.")

# Bir necha shartlarni ketma-ket yozish

inputAge = int(input("Yoshingiz nechada?\n"))
inputDay = input("Bugun qaysi kun?\n")
if inputAge<7 or inputAge>65 and inputDay.lower()=="chorshanba":
    print("Bugun muzey siz uchun bepul")