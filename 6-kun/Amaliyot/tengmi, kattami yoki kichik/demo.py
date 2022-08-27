print("Menga ikki ta raqam kiritsangiz\n"
      "ular teng yoki katta, kichikligini aniqlab beraman.\n\n")
inputNumber1 = int(input("Birinchi raqamni kiriting."))
inputNumber2 = int(input("Ikkinchi raqamni kiriting."))
if inputNumber1 == inputNumber2:
    print(f"{inputNumber1} soni {inputNumber2} soni bilan teng.")
elif inputNumber1 > inputNumber2:
    print(f"{inputNumber1} soni {inputNumber2} dan katta")
else:
    print(f"{inputNumber1} soni {inputNumber2} dan kichik")