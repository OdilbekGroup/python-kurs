# 8-dars
a = 20 # musbat son
b = -30 # manfiy son
c = 0 # 0 ga teng bo'lishi mumkin.
d = a + b
print(d, "\n")


# kvadrat yuzini hisoblaymiz
kvdrt_tmni = 25 # kvadrat tomoni 25 ga teng
kvdrt_yuzi = kvdrt_tmni**2 # kvadrat yuzini hisoblaymiz
print(kvdrt_yuzi, "\n")

pi = 3.14159 # o'nlik son (Float)
radius = 10 # butun son (Integer)
diametr = 2*radius
print(f"Aylana uzunligi {pi*diametr}ga teng\n")

# Butun sondan o'nlik songa
a = -20
b = 40
c = b / a
print(c, "\n") # natija o'nlik son bo'ladi

a = 2
b = 3.0
print(a+b)
print(a*b)
print(a**b)
print(2*(a+b))

aholi = 34_000_000
print(f"O'zbekiston aholisi {aholi}dan ortiq.")

# Konstanta
pi = 3.14159 # Konstanta
radius = 10

# Bir necha ozgaruvchiga qiymat  berish
x, y, z = 10, -10, -19.0

ism, yosh = "Olimjon", 16
print(f"{ism.title()}, {yosh} yoshda")

# typecasting

ism = "Javohir"
yosh = 19
xabar = ism + " " + str(yosh) + " yoshda"
print(xabar)

# type o'zgaruvchi turini tekshirish
ism = "Odilbek"
print(type(ism))

son = 123
print(type(son))
son = 123.9
print(type(son))

# input va sonlar

# Foydalanuvchidan tug'ilgan yilini so'raymiz.
t_yil = int(input("Tugilgan yilingizni kiriting. \n>>>"))
# Foydalanuvchi yoshini hisoblaymiz
yosh = 2022 - t_yil
# Foydalanuvchi yoshini konsolga chiqaramiz
print(f"Sizning yoshingiz {yosh} yoshda")

# boshqacha usul

# Foydalanuvchidan tug'ilgan yilini so'raymiz.
t_yil = input("Tugilgan yilingizni kiriting. \n>>>")
# t_yil o'zgaruvchisini integer ma'lumot turiga o'tkazamiz.
t_yil = int(t_yil)
# Foydalanuvchi yoshini hisoblaymiz
yosh = 2022 - t_yil
# Foydalanuvchi yoshini konsolga chiqaramiz
print(f"Sizning yoshingiz {yosh} yoshda")


