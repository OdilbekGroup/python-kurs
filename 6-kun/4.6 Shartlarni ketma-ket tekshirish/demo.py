# 4.6 Shartlarni ketma-ket tekshirish

narx = 15000
choy = True
salat = False
non = True
kompot = True
assorti = False

if choy:
    print("Mijoz choy oldi.")
    narx = narx + 3000
if salat:
    print("Mijoz salat oldi.")
    narx = narx + 5000
if non:
    print("Mijoz non oldi")
    narx = narx + 2000
if kompot:
    print("Mijoz kompot oldi")
    narx = narx + 5000
if assorti:
    print("Mijoz assorti oldi")
    narx = narx + 15000
print('Jami:', narx, "so'm")