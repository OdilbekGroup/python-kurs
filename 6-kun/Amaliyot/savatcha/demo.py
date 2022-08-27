products = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

basket = []
for n in range(5):
    basket.append(input(f"Savatga {n + 1}-mahsulotni qo'shing: "))

if basket:
    for product in basket:
        if product in products:
            print(f"Do'konimizda {product} bor")
        else:
            print(f"Do'konimizda {product} yo'q")
else:
    print("Savatingiz bo'sh")