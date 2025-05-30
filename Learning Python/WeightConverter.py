weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")

if unit == 'L':
    weight /= 2.205
    unit = "kg"
    print(f"Weight: {round(weight, 2)}{unit}")
elif unit == "K":
    weight *= 2.205
    unit = "lbs"
    print(f"Weight: {round(weight, 2)}{unit}")
else:
    print(f"{unit} is not a valid unit")
    
