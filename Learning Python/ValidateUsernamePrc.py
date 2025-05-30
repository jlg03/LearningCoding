#validate username
#no more then 12 char
#no spaces
#no digits

username = input("Enter a username: ")
len_username = len(username)
spaces_username = username.find(" ")
digits_username = username.isalpha()

if len_username >= 12:
    print("Invalid username, too long, must be less then 12.")
elif not spaces_username == -1:
    print("Invalid username, cannot contain any spaces")
elif digits_username == False:
    print("Invalid username, username cannot contain any numbers")
else:
    print(f"Welcome {username}")