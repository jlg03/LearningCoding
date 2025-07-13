employees = ["Eugene", "Squidward", "Spongebob", "Patrick"]

txt_data = "I like pizza"

file_path = "output.txt"


try:
    with open(file_path, "w") as file:
        for employee in employees:
            file.write(employee + "\n")
        print(f"File '{file_path}' created") 
except FileExistsError:
    print("That file already exists")

