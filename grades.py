percentage = int(input("Enter your percentage: "))
if percentage < 25:
    grade = "D"
elif percentage < 45:
    grade = "C"
elif percentage < 65:
    grade = "B"
elif percentage < 85:
    grade = "A"
else:
    grade = "A+"
print("Your grade is:", grade)