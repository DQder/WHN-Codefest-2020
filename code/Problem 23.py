vize = float(input("Vize giriniz: "))
finalNotu = float(input("Final notu giriniz: "))

if vize < 0 or vize > 100 or finalNotu < 0 or finalNotu > 100:
    print("Error : Puanlarınız 0-100 aralığında olmalıdır")

if ((vize * (30/100)) + (finalNotu * (70/100))) < 50:
    print("Kaldınız")
else:
    print("Geçtiniz")