
print("##____Body Mass Index______##")

Height = float(input("Your Height in m: "))
Weight = int(input("Your Weight in Kg: "))


BMI = Weight/Height **2

print(f"BMI = {BMI}") #rounding to 2 digits after the decimal  

if BMI == 30 or BMI > 30:
    print("Obesity")
elif BMI > 25 and BMI < 29:
    print ("Overweight")
elif BMI > 18.5 and BMI < 25:
    print("Normal")
else:
    print("Underweight")
    