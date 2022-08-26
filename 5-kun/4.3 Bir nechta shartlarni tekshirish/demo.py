# 4.3 Bir necha shartlarni tekshirish

# print('3 ta ixtiyoriy son kiriting \nva u qanday son ekanini bilib oling.')
# for n in range(3):
#     inputNumber = int(input("Ixtiyoriy son kiriting.\n>>>"))
#     if inputNumber > 0:
#         print("Bu son musbat")
#     elif inputNumber < 0:
#         print('Bu son manfiy')
#     else:
#         print('Bu son 0 ga teng')

age = int(input("Yoshingiz nechida"))
if age<5:
    price = "bepul"
elif age<12:
    price = '5000 UZS'
elif age<40:
    price = "10000 UZS"
else:
    price = "8000 UZS"
print(f"Sizga kirish {price}")

# Biz else siz ham ishlayveramiz.

age = int(input("Yoshingiz nechida"))
if age<5:
    price = "bepul"
elif age<12:
    price = '5000 UZS'
elif age<40:
    price = "10000 UZS"
elif age>40:
    price = "8000 UZS"
print(f"Sizga kirish {price}")
