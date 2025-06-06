# Weight converter

weight = float(input('Enter Your weight'))
unit = input('Kilograms or Pounds? (K / L):') # writing "or" - "/" is the same 

# 1 kg = 2.205 Lbs

if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"
    print(f"your weight is: {round(weight, 1)} {unit}")

elif unit == "L":
    weight = weight / 2.205
    unit = "kg"
    print(f"your weight is: {round(weight, 1)} {unit}")

else:
    print(f"{unit} was not valid")

