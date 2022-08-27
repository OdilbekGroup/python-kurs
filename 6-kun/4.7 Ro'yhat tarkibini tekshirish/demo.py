# 4,7 Ro'yhat tarkibini tekshirish
# in operatori

menu = ('manti', 'osh')
if 'manti' in menu: # osh menyuda bormi
    print(True)
if 'qovurdoq' in menu: # osh menyuda bormi
    print(True)
else:
    print(False)
# Menda nimagadir shartsiz konsolda chiqmadi. Menda xatolik berdi.
# Ammo qanday xato ekanini aytmadi.
# Shuning uchun in operatorini shart bilan yozdim

# menu = ["manti", 'osh', 'chuchvara', "tovuq sho'rva", "kabob"]
# inputOrder = input("Qaysi ovqatga buyurtma berasiz?\n>>> ")
# if inputOrder.lower() in menu:
#     print("Buyurtmangiz qabul qilindi.!")
# else:
#     print("Bizda unday ovqat yo'q")

# not in operatori
# menu = ["manti", 'osh', 'chuchvara', "tovuq sho'rva", "kabob"]
# inputOrder = input("Qaysi ovqatga buyurtma berasiz?\n>>> ")
# if inputOrder.lower() not in menu:
#     print("Bizda unday ovqat yo'q")
# else:
#     print("Buyurtmangiz qabul qilindi!")

# Ikkala ro'yhatni solishtirish
menu = ["manti", 'osh', 'chuchvara', "tovuq sho'rva", "kabob"]
orders = ["manti", 'osh', "kabob", "so'msa", "varaqi"]

for order in orders:
    if order in menu:
        print(f"Menyuda {order} bor")
    else:
        print(f"Menyuda {order} yo'q")

# Ro'yhat bo'sh emasligini tekshirish

list1 = [1, 2, 3]
list2 = []
if list1:
    print(True)
if list2:
    print(True)
else:
    print(False)
# Bu yerda len orqali shartlarsiz ro'yhat bo'sh emasligini
# tekshirishim kerak edi.
# Lekin omadim kelmadi.

menu = ["manti", 'osh', 'chuchvara', "tovuq sho'rva", "kabob"]
orders = ["manti", 'osh', "kabob", "so'msa", "varaqi"]

if orders:
    for order in orders:
        if order in menu:
            print(f"Menyuda {order} bor")
        else:
            print(f"Menyuda {order} yo'q")
# orders o'zgaruvchisi saqlayotgan ro'yhat bo'sh bo'lsa shart bajarilmaydi.


