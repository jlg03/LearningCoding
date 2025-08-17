import datetime



def main_menu(list_expeses):
    print("Select what you want to do")
    print()
    print("1. Add an expense")
    print()
    print("2. Update an expense")
    print()
    print("3. Delete an expense")
    print()
    print("4. View all expenses")
    print()
    print("5. View summary of all expenses")
    print()
    print("6. View summary of expense for a specific month (in the current year)")
    print()
    print("7. Quit")
    user_selection = input("Enter your selection: ")
    
    if user_selection == "1":
        description = input("Description: ")
        amount = float(input("Enter amount: "))
        add_expense(description=description, amount=amount, list_expenses=list_expenses)
    elif user_selection == "2":
        list_expense(date=, list_expenses=list_expenses)
        update_expense(date=, id=, amount=,  list_expenses=list_expenses)
    elif user_selection == "3":
        list_expense(date=,  list_expenses=list_expenses)
        delete_expense(date=, id=,  list_expenses=list_expenses)
    elif user_selection == "4":
        list_expense(list_expenses=list_expenses)
    elif user_selection == "5":
        total_expense(list_expenses=list_expenses)
    elif user_selection == "6":
        total_expense_month(month=, list_expenses=list_expenses)
    elif user_selection == "7":
        quit()
    else:
        print("That was an invalid input")
    
    

def add_expense(description, amount, list_expenses):
    
    # id number = 1
    # date = getdate
    # if date already exist in list
    #     id number =  last current id number + 1
    #     add description and amount to list
    #     return list back to main menu
    # else
    #     create list
    #     add id, date, description, amount
    #     return list back to main menu
    
    # list needs: 
    # ID  date  description amount
    
    
def list_expense(date, list_expenses):
    # if date not empty list expenses for selected date
    # else list all expenses recorded
    
def total_expense_month(month, list_expenses):
    # list all expenses of the selected month of the current year
    
def total_expense(list_expenses):
    # list all expenses ever made
    
def update_expense(date, id, amount, list_expenses):
    # from the chosen date and id update the amount that was selected
    
def delete_expense(date, id, list_expenses):
    # from the selected date and id delete the specific amount


list_expenses = []
main_menu(list_expenses)