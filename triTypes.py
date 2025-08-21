A = int(input("Enter first angle: "))
B = int(input("Enter second angle: "))
C = int(input("Enter third angle: "))

if A + B + C != 180:
    print("Not a valid triangle")
elif A == 90 or B == 90 or C == 90:
    print("Right Triangle")
elif A > 90 or B > 90 or C > 90:
    print("Obtuse Triangle")
else:
    print("Acute Triangle")
