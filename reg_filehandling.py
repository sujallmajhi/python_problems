#  requirements
# ask user if they want to register or login
# if register, ask user for name rw password and store it in a file parmanently
#  if login, ask username rw password and check if it exist in the file, if it does print login success if not print invalid credientials
# if the user is valid then show them 3 options 1, check balance, 2. add balance
#  if option is check, print the amount of that user
# if optin is add, ask the user amount to add in the account and add it with current balance
import os
import json

filepath = "users.json"  # file path

def reg():
    # taking input for registration
    name = input("Enter name: ")
    password = input("Enter password: ")

    # check if file exists and is non-empty
    if os.path.exists(filepath) and os.stat(filepath).st_size > 0:
        with open(filepath, 'r') as file:
            users = json.load(file)
    else:
        users = []

    # check if the username already exists
    for user in users:
        if user["name"] == name:
            print("A user with the same name already exists")
            return  # return to the main loop

    # append the new user to the list
    users.append({"name": name, "password": password})

    # write the updated list of users back to the file
    with open(filepath, "w") as file:
        json.dump(users, file, indent=4)  # correctly serialize the JSON data
             
def login():
    # taking input for login
    name = input("Enter name: ")
    password = input("Enter password: ")

    # check if file exists and is non-empty
    if os.path.exists(filepath) and os.stat(filepath).st_size > 0:
        with open(filepath, 'r') as file:
            users = json.load(file)
    else:
        print("No users registered yet!")
        return  # No users to log in to

    # check if the username and password match any registered user
    for user in users:
        if user["name"] == name and user["password"] == password:
            print(f"Welcome {name}!")
            

while True:
    print("Choose an option:")
    print("1::Register")
    print("2::Login")
    
    choice = int(input("1/2: "))
    if choice == 1:
        reg()
    elif choice == 2:
        login()
    else:
        print("Please enter a valid choice")
        continue  # prompt the user again

