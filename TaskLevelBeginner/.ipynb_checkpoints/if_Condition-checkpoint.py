print("##1.____Body Mass Index______##")

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


print("##2.____To determine which country a city belongs to.______##")

Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]


City_name = input("Enter a city name: ")

if City_name in Australia:
    print(f"{City_name} is in Australia")

elif City_name in UAE:
    print(f"{City_name} is in UAE")
else:
    print(f"{City_name} is in India")
    














