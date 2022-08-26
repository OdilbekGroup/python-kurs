# 3.8 Tuples - o'zgarmas ro'yhatlar

numbers = (1, 2, 3, 4, 5, 6)
print(numbers)
print(numbers[0])

sonlar = (1, 2, 3, 4, 5, 6)
print(sonlar[-1])
print(sonlar[:3])
print(sonlar[0:])

# O'zgarmas ro'yhatni o'zgartirish
sonlar = list(sonlar)
sonlar[0] = 8
sonlar = tuple(sonlar)
print(sonlar)

# AMALIYOT
toys = ('bear', 'doll', 'train', 'plain') # tuple
print(toys)
toys = list(toys) # list
toys[3] = "car"
print(toys)
toys = tuple(toys) # tuple
print(toys)
