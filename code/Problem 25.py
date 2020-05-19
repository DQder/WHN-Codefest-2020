ders = input("Ders ismi giriniz: ")
vize = float(input("Vize giriniz: "))
finalNotu = float(input("Final notu giriniz: "))

vize = (vize * (30/100))
finalNotu = (finalNotu * (70/100))

print(ders, "ortalamanız:", (vize + finalNotu))