# 3.7 ro'yhatlar bilan ishlash

# Ro'yhatlarni tartiblash
harflar = ["I", "O", "S", "F", "R"]
print(f"Tartiblanmagan ro'yhat {harflar}")
harflar.sort()
print(f"Tartiblangan ro'yhat {harflar}\n")


harflar = ["I", "O", "S", "F", "R"]
print(f"Tartiblanmagan ro'yhat {harflar}")
harflar.sort(reverse=True)
print(f"Teskari tartiblangan ro'yhat {harflar}\n")
harflar = ["I", "O", "S", "F", "R"]
print(f"Tartiblangan ro'yhat {sorted(harflar)}\n"
      f"Asl ro'yhat o'zgarmaydi {harflar}\n")


print(f"Tartiblanmagan ro'yhat {harflar}")
harflar.sort()
print(f"Teskari tartiblangan ro'yhat {sorted(harflar, reverse=True)}\n"
      f"Asl ro'yhat o'zgarmaydi {harflar}\n")

numbers = [2, 5, 8, 2, 1, 4, 5, 7, 3, 4,]
print(numbers)
numbers.sort()
print(numbers)
print(sorted(numbers), "\n")

# Ro'yhatni aylantirish]

fruits = ["Anjir", "shaftoli", "olma", "Behi"]
print(fruits)
fruits.reverse()
print(fruits, "\n")

# Ro'yhatning uzunligini topish
numbers = [2, 5, 8, 2, 1, 4, 5, 7, 3, 4, 2, 5, 8, 2, 1, 4, 5, 7, 3, 4, 2, 5, 8, 2, 1, 4, 5, 7, 3, 4]
print(f"{numbers}" "\n"
      f"Elementlar soni {len(numbers)} ta \n")

# Sonlarni tez yozish
numbers = list(range(0, 101))
print(numbers, '\n')

# Toq va juft sonlarni chiqarish
juft_son = list(range(0, 20, 2))
toq_son = list(range(1, 20, 2))
print(f"Juft sonlar {juft_son} \n"
      f"toq sonlar {toq_son}\n")

# Sonli ro'yhat ustida sodda amallar
narxlar = [12000, 11000, 22000, 5555, 555555]
arzon = min(narxlar)
qimmat = max(narxlar)
jami = sum(narxlar)
print(f"Eng arzon narx {arzon}\n"
      f"eng qimmati {qimmat}\n"
      f"jami {jami}\n")


narxlar = [12000, 11000, 22000, 5555, 555555,12000, 11000, 22000, 5555, 555555]
print(narxlar)
narx = narxlar[0:3]
print(narx)
print(narxlar[2:6])
print(narxlar[:6])
print(narxlar[2:])

# RO'yhatdan nusxa olish
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
numbers1 = numbers
numbers1.append(0)
numbers1.append(10)
print(f"Oldingi sonlar: {numbers}\n"
      f"Yangi sonlar: {numbers1}\n")
# Kutilgan natija bo'lmadi
# Boshqa usuldan foydalanamiz

numbers1 = numbers[:]
numbers1.append(11)
numbers1.append(12)
print(f"Oldingi sonlar: {numbers}\n"
      f"Yangi sonlar: {numbers1}\n")