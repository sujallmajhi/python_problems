# Add items to the cart (item name, price, quantity).
# Remove items from the cart by item name.
# Display the total 
carts=[]

def add_items():
    item = input("Enter an item to add: ").lower()  # Make the item input lowercase
    price = int(input("Enter a price: "))
    quantity = int(input("Enter a quantity: "))
    carts.append({"item": item, "price": price, "quantity": quantity})
    return carts

def remove_item(carts):
    item_remove = input("Enter an item to remove: ").lower()  # Make the remove item input lowercase
    found = False  # Flag to track if the item is found
    for i in carts:
        if i["item"].lower() == item_remove:  # Case-insensitive comparison
            carts.remove(i)
            print(f"{i['item']} removed.")
            found = True
            break  # Break after finding the first match
    if not found:
        print("Enter a valid item:")

def display(carts, total):
    for i in carts:
        total += i["price"] * i["quantity"]
    return total

while True:
    carts = add_items()
    remove = input("If you want to remove an item (y/n): ").lower()
    if remove == "y":
        remove_item(carts)
    quit = input("If you want to quit (y/n): ").lower()
    if quit == "y":
        break  # Exit the loop if 'y' is entered
    else:
        continue  # Continue the loop

total = display(carts, total=0)   
print(f"Your total is {total}") 
print("Thanks for shopping!!!!!!!!!!!!")
