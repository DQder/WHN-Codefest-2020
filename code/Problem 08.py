vize = float(input("Vizeyi giriniz: "))
if vize > 100 or vize < 0:
    print("Error : Vizeniz 0-100 aralığında olmalıdır.")
finalNotu = float(input("Final notunu giriniz: "))
if finalNotu > 100 or finalNotu <0:
    print("Error : Final notunuz 0-100 aralığına olmak zorundadır.")

sonNot = (finalNotu + vize)/2

if finalNotu < 50:
    print("Kaldınız")
else:
    if sonNot < 50:
        print("Kaldınız")
    elif sonNot >= 50:
        print("Geçtiniz")