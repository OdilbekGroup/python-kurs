listLogin = ["Odilbek", "Murodali", "Quvonch", 'Nodir', 'Azamat']
inputLogin = input("Marhamat, o'zingizga yoqqan loginni tanlang.")
if inputLogin.title() in listLogin:
    print("Ushbu login band")
else:
    print("Xush kelibsiz, " + inputLogin)