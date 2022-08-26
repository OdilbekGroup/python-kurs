# 5-dars
a = "5-dars"
print(a)
print(" ")
# ijodiy a,alliyot

qator1 = "Nima qilsa butun dunyo bo'ylab chop etilgan kitoblarni o'qish \nmumkin ?"
qator2 = "Hozirgi kunda dunyo bo'ylab juda ko'plab turdagi kitoblar chop \netilgan. Ularni sifatli tarzda quyidagi sayt orqali (http://nap.edu/) topishingiz mumkin"
qator3 = "Saytda ko'plab yozuvchilarning xilma-xil asarlari mavjud. Kitoblarni \nnomi, mavzusi yoki avtori orqali topish mumkin."
qator4 = "Kitobxon do'stlaringizga yuboring 🤓"
qator5 = "© @Nimaqilsa | Foydali, qiziqarli, kreativ !"
print(f"{qator1} \n\n {qator2} \n\n {qator3} \n\n {qator4} \n\n {qator5}")
print("\n \n")


ism = "Odilbek"
familya = "Xudaybergenov"
uzun_ismim = ism + " " + familya
print("Ism= familyam " + uzun_ismim)

print("Hammaga \tsalom")

# .upper() metodi
print("6-dasr".upper())

# .title() metodi
ism = "odilbek xudaybergenov"
print(ism.title())

# .capitalize() metodi
ism = "odilbek xudaybergenov"
print(ism.capitalize())

# .lower() metodi
ism = "Odilbek Xudaybergenov"
print(ism.lower())

# strip(), rstrip() va lstrip() metodlari

texnika1 = "        kompyuter        "
print("Men " + texnika1.lstrip() + "da ishlashni yoqtiraman.")
print("Men " + texnika1.rstrip() + "da ishlashni yoqtiraman.")
print("Men " + texnika1.strip() + "da ishlashni yoqtiraman.")

texnika1 = texnika1.strip()
texnika1 = "Men " + texnika1.strip() + "da ishlashni yoqtiraman."
print(texnika1)

# 7-dars
# ism = input('Ismingiz kim?')
# print(f"Assalomu alaykum, {ism}")

# ism = input('Ismingiz kim?\n >>>')
# print(f"Assalomu alaykum, {ism}")

# amaliyot
# 1
# kocha = "Bog'bon"
# mahalla = "Sag'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# 2
#  print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
# 3
# kocha = input("Ko'changiz nomini kiriting.\n >>>")
# mahalla = input("Mahallangiz nomini kiriting. \n >>>")
# tuman = input("Tumaningiz nomini kiriting. \n >>>")
# viloyat = input("Viloyatingiz nomini kiriting.\n >>>")
# print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati")
# 4
# kocha = "Bog'bon"
# mahalla = "Sag'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani, \n{viloyat} viloyati")
# 5-6
manzil = f"Qoraqalpog'iston Respublikasi Beruniy tumani".upper()
print(manzil)
manzil = f"Qoraqalpog'iston Respublikasi Beruniy tumani".title()
print(manzil)
manzil = f"Qoraqalpog'iston Respublikasi Beruniy tumani".lower()
print(manzil)
manzil = f"Qoraqalpog'iston Respublikasi Beruniy tumani".capitalize()
print(manzil + "\n")
manzil = manzil.upper()
print(manzil)
manzil = manzil.lower()
print(manzil)
manzil = manzil.title()
print(manzil)
manzil = manzil.capitalize()
print(manzil)
