def main_menu():
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.\nYou have 5 chances to guess the correct number")
    print()
    print("Please select the difficulty level: \n1. Easy (10 chances)\n2. Medium (5 chances)\n3. Hard (3 chances)\n4. Quit")
    print()
    user_input = input("Enter your choice: ")
    
    if user_input == "1":
        pass
    elif user_input == "2":
        pass
    elif user_input == "3":
        pass
    elif user_input == "4":
        quit
    else:
        print("That was an invalid input please try again")


main_menu()