meyveler = ["muz", "elma", "üzüm"]
ist = input("Meyve giriniz: ")
if ist not in meyveler:
    print("Error : Bu meyveden manavımızda yoktur!")
else:
    if ist == meyveler[0]:
        kilo = float(input("Gaç kilo alcağını gir: "))
        print("Mehmet", str(kilo) + "kg", ist, "aldı ve toplamda", str(kilo * 5) + "₺", "ödedi.")
        exit()
    elif ist == meyveler[1]:
        ElmaRenkleri = ["kırmızı", "sarı", "yeşil"]
        ElmaRengi = input("Elmanın rengini giriniz: ")
        if ElmaRengi not in ElmaRenkleri:
            print("Error : Girdiğiniz elma rengi elimizde yok!")
        else:
            kilo = float(input("Gaç kilo alcağını gir: "))
            print("Mehmet", str(kilo) + "kg", ist, "aldı ve toplamda", str(kilo * 2) + "₺", "ödedi.")
            exit()
    elif ist == meyveler[2]:
        UzumRenkleri = ["mor", "yeşil"]
        UzumRenk = input("Üzümün rengini giriniz: ")
        if UzumRenk not in UzumRenkleri:
            print("Error : Girdiğiniz üzüm rengi elimizde yok!")
        else:
            if UzumRenk == UzumRenkleri[0]:
                kilo = float(input("Gaç kilo alcağını gir: "))
                print("Mehmet", str(kilo) + "kg", ist, "aldı ve toplamda", str(kilo * 3) + "₺", "ödedi")
            else:
                kilo = float(input("Gaç kilo alcağını gir: "))
                print("Mehmet", str(kilo) + "kg", ist, "aldı ve toplamda", str(kilo * 3.5) + "₺", "ödedi")