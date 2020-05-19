sın1 = float(input("Birinci sınav notunu giriniz: "))
sın2 = float(input("İkinci sınav notunu giriniz: "))
okulPuan = 0

sozlu = float(input("Sözlü notunu giriniz: "))

if (sın1 < 0 or sın2 > 100) or (sozlu < 0 or sozlu > 100):
    print("Error : Girdiğiniz notlar 0-100 aralığında olmalıdır")

sinavlar = [sın1, sın2]

for x in sinavlar:
    okulPuan += (x * (40/100))

okulPuan += (sozlu * (20/100))

if okulPuan < 50:
    print("Kaldınız")
    print("Notunuz:", okulPuan)
else:
    print("Geçtiniz")
    print("Notunuz:", okulPuan)