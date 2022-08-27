inputAge = int(input("Yoshingiz nechada? "))
if inputAge < 4 or inputAge > 60:
    print('Muzeyga kirish bepul')
elif inputAge < 18:
    print('Muzeyga kirish 10000')
elif inputAge > 18:
    print("Muzeyga kirish 20000")