print("Menga son kiriting va men u sonning 2 dan 11 gacha bo'lgan\n "
      "sonlardan qaysilariga qoldiqsiz bo'linishini aniqlab beraman.")

inputNumber = int(input("Butun son kiriting.\n>>>"))
for n in range(2,12):
    if not(inputNumber % n):
        print(f"{inputNumber} soni {n} soniga qoldiqsiz bo'linadi.")