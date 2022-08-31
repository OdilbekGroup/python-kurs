# 5.3 To'plamlar

numbers = {1, 2, 3}
print(numbers)
names = {'Alijon', "Valijon", "Boqijon"}
print(names)

numbers ={1, 2, 3, 4, 4, 5, 5, 5, 6}
print(numbers)

none = set()


fruits = ['olma', 'olma', 'anjir', 'anjir', 'uzum', 'uzum']
fruits = set(fruits)
print(fruits)

fruits = list(fruits)
print(fruits)
# To'plamga element qo'shish
fruits = set(fruits)
fruits.add("anor") # Bitta element qo'shish
print(fruits)
fruits.update(['nok', 'shaftoli'])
print(fruits)

# To'plamdan element o'chirish
fruits.discard("nok")
print(fruits)
fruits.remove("anjir")
print(fruits)

print(numbers)
numbers.discard(2)
print(numbers)
numbers.remove(1)
print(numbers)

# Tasodifiy elementni sug'urib olish
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
number = numbers.pop()
print(number)
# To'plamlarni birlashtirish
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b = {1, 2, 3, 4, 5, 6, 7, 8, 9}
c = a.union(b)
print(c)
# To'plamlar ichidan bir xil elementlarni topish
a = { 5, 6, 7, 8, 9}
b = { 4, 5, 6, 7}
print(a&b)
d = a.intersection(b)
print(d)
# Endi bir to'plamda bor ikkinchisida yo'q elementlarni aniqlaymiz
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a-b) #bu yerda faqat a da borini ko'r'satadi.
print(a.difference(b)) # Bu amalni metod orqali bajarish

# Endi simemtrik farqni aniqlaymiz
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a^b)
print(a.symmetric_difference(b))

# amaliyot
color = {'black', 'red', 'dark'}
print(color)
color.add('blue')
print(color)
color.update({"yellow", 'green'})
print(color)

number1 = {10, 20, 30, 40, 50}
number2 = {30, 40, 50, 60, 70}
numbers = number1.intersection(number2)
print(numbers)

print(number1.difference(number2))
print(number1^number2)


buy = {'un', 'guruch', 'yog', 'kartoshka', 'olma', 'anor'}
products = {'un', 'guruch', 'olma', 'anor', 'anjir', 'pomidor', 'CoCaCoka'}

my_products = buy.intersection(products) #Sotib olganlarim
my_products = list(my_products)
print(f'Sotib olganlarim {my_products}')

no_products = buy.difference(products) #do'konda yo'q mahsulotlar
no_products = list(no_products)
print(f"Do'konda yo'q {no_products}")

products.update(['yog', 'kartoshka'])
new_products = products.difference(no_products)
print(f'Yangi mahsulotlar {products.intersection(no_products)}')


