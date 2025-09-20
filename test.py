from datetime import date, datetime

list_expenses = []
id_number = 1
today_date = date.today()
if len(list_expenses) == 0:
    list_expenses.append([today_date,[id_number, 2, 3]])
    
print(list_expenses)
print(list_expenses[0])
print(list_expenses[0][0])
print(list_expenses[0][1][0])