points = float(input("Öğrencinin puanını giriniz: "))

if points < 0 or points > 100:
    print("Error : Öğrencinin notu 0-100 aralığında olmalıdır")
    exit()

if points < 50:
    print("Kaldınız")
else:
    print("Geçtiniz")