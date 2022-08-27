# $.5 Boolean(Mantiqiy) ma'lumotla r turi

a = True
b = False

narx = 15000
choy = True
solat = False

if choy and solat:
    narx = narx + 10000
elif choy or solat:
    narx = narx + 5000
print(f"Jami: {narx} so'm")