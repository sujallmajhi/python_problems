#  requirements
# ask user if they want to register or login
# if register, ask user for name rw password and store it in a file parmanently
#  if login, ask username rw password and check if it exist in the file, if it does print login success if not print invalid credientials
# if the user is valid then show them 3 options 1, check balance, 2. add balance
#  if option is check, print the amount of that user
# if optin is add, ask the user amount to add in the account and add it with current balance
import os
import json

filepath = "users.json"

# Register function
def register():
    name = input("Enter name: ")
    password = input("Enter password: ")
    
    # Check if file exists and is non-empty
    if os.path.exists(filepath) and os.stat(filepath).st_size > 0:
        with open(filepath, 'r') as file:
            users = json.load(file)
    else:
        users = []  # Initialize as an empty list if file is empty or does not exist
    
    # Check if user already exists
    for user in users:
        if user["name"] == name:
            print("User with this name already exists.")
            return

    # Append new user to the list
    users.append({"name": name, "password": password, "balance": 0})
    
    # Write the updated list of users back to the file
    with open(filepath, 'w') as file:
        json.dump(users, file, indent=4)

    print("Registration successful!")

# Login function
def login():
    name = input("Enter name: ")
    password = input("Enter password: ")

    if os.path.exists(filepath) and os.stat(filepath).st_size > 0:
        with open(filepath, 'r') as file:
            users = json.load(file)

        # Find user matching name and password
        for user in users:
            if user["name"] == name and user["password"] == password:
                print("Login successful!")
                return user  # Return the user object if credentials match
        
    print("Invalid name or password.")
    return None

# Check balance function
def check_balance(user):
    print(f"Your balance is {user['balance']}")

# Add balance function
def add_balance(user):
    add = int(input("Enter balance you want to add: "))   
    user['balance'] += add
    print(f"Your balance = {user['balance']}")

# Withdraw balance function
def withdraw(user):
    withdraw_amount = int(input("Enter amount you want to withdraw: ")) 
    if user['balance'] >= withdraw_amount:
        user['balance'] -= withdraw_amount
        print(f"Your current balance = {user['balance']}")
    else:
        print("Insufficient balance!")

# Main loop
while True:
    print("1. Register")
    print("2. Login")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        register()
    elif choice == "2":
        user = login()

        if user:
            print("1. Check Balance")
            print("2. Add Balance")
            print("3. Withdraw Balance")
            print("4. Logout")
            
            option = input("Enter 1 to 4: ")
            if option == "1":
                check_balance(user)
            elif option == "2":
                add_balance(user)
            elif option == "3":
                withdraw(user)
            elif option == "4":
                print("Thanks for using NABIL BANK!!!!")
                break
            else:
                print("Enter a valid choice!")
            
            # After each operation, save the updated user back into the file
            with open(filepath, 'r') as file:
                users = json.load(file)

            for idx, u in enumerate(users):
                if u["name"] == user["name"]:
                    users[idx] = user

            with open(filepath, 'w') as file:
                json.dump(users, file, indent=4)

        else:
            print("Failed to login. Please try again.")
    else:
        print("Enter a valid choice!")
