oyunlar = ["CS:GO", "Garrys Mod", "Euro Truck"]
oyun = input("Oyun: ")
if oyun not in oyunlar:
    print("Error : Steam bütün oyunları içerdiğine rağmen Steam'in bu çakma versiyonunda girdiğiniz oyun yok!")
else:
    if oyun == oyunlar[0]:
        print("Bu oyunun üç versionu vardır.")
        versiyonlar = ["v1.0", "v2.0", "v3.0"]
        versiyon = input("Versiyon giriniz: ")
        if versiyon not in versiyonlar:
            print("Error : Steam'de bu oyun versiyonu bulunmamaktadır!")
        else:
            if versiyon == (versiyonlar[0] or versiyonlar[1]):
                print("Fiyat: 30₺")
            else:
                print("Fiyat: 40₺")
    elif oyun == oyunlar[1]:
        print("Bu oyunun tek versionu vardır.\nFiyat: 15₺")
    elif oyun == oyunlar[2]:
        print("Bu oyunun iki versiyonu vardır.")
        versiyonlar = ["v1.0", "v2.0"]
        versiyon = input("Versiyon giriniz: ")
        if versiyon not in versiyonlar:
            print("Error : Steam'de bu oyun versiyonu bulunmamaktadır.")
        else:
            print("Fiyat: 20₺")