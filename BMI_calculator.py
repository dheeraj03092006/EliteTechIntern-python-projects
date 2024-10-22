def bmiCalculator(height, weight):
    height /= 100
    bmi = weight / height**2
    return round(bmi, 1)

height = float(input("Please enter your height in Centimeters: "))
weight = float(input("Please enter your body weight: "))
bmi = bmiCalculator(height, weight)
print("Your BMI is: ",bmi)
print("According to World Health Organisation ",end="")
if bmi<18.5:
    print("you are underweight")
elif 18.5 <= bmi <24.9:
    print("you have normal weight")
elif 24.5 <= bmi < 29.9:
    print("you are overweight")
else:
    print("you are obese")