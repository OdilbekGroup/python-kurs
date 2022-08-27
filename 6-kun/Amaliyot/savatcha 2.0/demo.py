products = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

basket = []
for n in range(5):
    basket.append(input(f"Savatga {n + 1}-mahsulotni qo'shing: "))

thereAre = []
thereAreNot = []
for product in basket:
    if product in products:
        thereAre.append(product)
    else:
        thereAreNot.append(product)

if thereAreNot:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for product in thereAreNot:
        print(product)
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")