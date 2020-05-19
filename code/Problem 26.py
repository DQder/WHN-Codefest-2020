# Ne kadar çok sınav puanı girişi yapılması gerekiyorsa bu program o kadar verimli
i = 0
TopNot = 0
sınavSay = float(input("Puanını gireceğiniz sınav sayısını yazınız: "))

while i < 5:
    Not = float(input("Not giriniz: "))
    if not 0 <= Not <= 100:
        print("Error : Girdiğiniz sınav notlar 0-100 aralığında olmalıdır")
        continue
    TopNot += Not
    i += 1
TopNot = (TopNot / i)
print(TopNot)


def beslik(toplam):
    if 0 <= toplam < 50:
        print("Puanınız: 0")
    elif toplam == 100:
        print("Puanınız: 5")
    else:
        l = 0
        beslikNotu = 1
        birinci = 50
        ikinci = 60
        while l < 5:
            if birinci <= toplam < ikinci:
                print("Puanınız:", beslikNotu)
                exit()
            else:
                birinci += 10
                ikinci += 10
                beslikNotu += 1
                l += 1


beslik(TopNot)