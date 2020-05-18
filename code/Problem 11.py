speed = float(input("Enter your speed (km/h): "))
distance = float(input("Enter the distance between you and the target (km): "))

if speed < 0:
    print("\nError : Your speed cannot be lower than 0.")
    exit()
if distance < 0:
    print("\nError : Your distance cannot be lower than 0.")
    exit()

time = distance / speed

if 0 < time <1:
    time *= 60
    print("\nYou will arrive to your destination in", time, "minutes.")
else:
    print("\nYou will arrive at your destination in", time, "hours.")