import math

Hs = float(input("Enter the height of the cylinder (cm): "))
Rs = float(input("Enter the radius of the cylinder (cm): "))

CylinderField = 2 * math.pi * Rs * (Rs + Hs)
CylinderVolume = math.pi * Rs**2 * Hs

print("Silinirin alanı:", CylinderField)
print("Silindirin hacmi:", CylinderVolume)