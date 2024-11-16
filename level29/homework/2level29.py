

weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))


bmi = weight / (height ** 2)


if bmi < 50.0:
    print("Underweight")
elif bmi < 75.0:
    print("Normal weight")
elif bmi < 100.0:
    print("Overweight")
else:
    print("Obesity")
