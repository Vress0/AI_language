perpound2Kg = 0.45359237
perinch2meter = 0.0254

weight = float(input("Weight (pounds): "))
height = float(input("Height (inches): "))
bmi = weight * perpound2Kg / (height * perinch2meter) ** 2
print('BMI:', bmi)
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi  < 30:
    print("Overweight")
else:
    print("Obese")
