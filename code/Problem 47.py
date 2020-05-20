N = int(input("Enter a number: "))
tekToplam = 0
tekCarp = 1
ciftKTop = 0
for x in range(1, N, 2):
    tekToplam += x
    tekCarp *= x
    ciftKTop += (x**2)
print("Tek sayıların toplamı:", tekToplam, "\nTek sayıların çarpımı:", tekCarp,
      "\nÇift sayıların karelerinin toplamı:", ciftKTop)

