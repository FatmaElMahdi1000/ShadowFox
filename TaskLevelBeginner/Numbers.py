print("---Numbers 1---")
def numbers(num, formatting):
    return format(num, formatting)

number = 145
formatting = 'o'  #octal representation of a number 
Final = numbers(number, formatting)
print(Final)


print("---Numbers 2---")

def Pond_Area(radius):
    pi = 3.14
    Area = int(pi * (radius**2)) #square meters (area is in square unit)
    water_total_amount = int(Area * 1.4)
    return Area, water_total_amount

radius = 84
Result = Pond_Area(radius) # m²
print(Result) 

print("---Numbers 3---")
Distance = 490 #meterlong
Time = 7 #min 
Time_in_sec = 7 * 60 
speed = int(Distance/Time_in_sec) #distance/time 
print(f"Speed is going to be {speed}")












