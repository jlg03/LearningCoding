unit = input("Current unit of measurement (C or F): ")
temp = float(input("Current temperature: "))

if unit == "C":
    temp = (temp * (9/5) + 32)
    unit = "F"
    print(f"Temperature: {round(temp, 2)}°{unit}")
elif unit == "F":
    temp = (temp - 32) * (5/9)
    unit = "C"
    print(f"Temperature: {round(temp, 2)}°{unit}")
else:
    print(f"{unit} is not a valid unit")
