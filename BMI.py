#BMI = weight in kgs / (height in m)^2
weight = float(input("Enter weight in kgs"))
height = float(input("Enter weight in meters"))

bmi = weight / (height * height)
print(f"BMI is {bmi}")