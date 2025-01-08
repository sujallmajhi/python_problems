# food items (using a dictionary instead of a set)
food = {"meat": 200, "icecream": 50, "thakali": 500}

# beverage items (using a dictionary instead of a set)
beverage = {"coke": 40, "beer": 60, "water": 20}

cart=[]
total_cost=0
# Function for displaying food items
def display_food():
    print("----------FOOD ITEMS --------------")
    for key, value in food.items():
        print()
        print(f"{key}: ${value}")
        print()

# Function for displaying beverage items
def display_beverage():
    print("----------BEVERAGE ITEMS ----------")  
    for key, value in beverage.items():
        print()
        print(f"{key}: ${value}")
        print()

def add_to_cart(item,price):
    global total_cost
    cart.append((item,price))   #cannot accept two arguments so using two dimensional tuple
    total_cost+=price 
    print(f"{item}:${price} added to your lsit ")  

while True:
    print("------WELCOME TO SUJALCAFE-------")
    print()
    print("1.Food:")
    print("2.Beverage:")
    choice=int(input("1 or 2="))
    if choice==1:
        display_food()
        while True:
            item=input("Enter a item:").lower()
            if item in food:
             add_to_cart(item,food[item])
            else:
                print("Enter a valid item!!!")
            quit=input("If you want to exit the food section y/n:").lower()  
            if quit=="y":
                False
                break
            else:
                continue  
        
    elif choice==2:
        display_beverage()
        while True:
            item=input("Enter a item:").lower()
            if item in beverage:
                add_to_cart(item,beverage[item])
            else:
                print("Enter a valid item") 
            quit=input("if you want to quit beverage section y/n:").lower()   
            if quit=="y":
                False
                break
            else:
                continue    
            
    else:
        print("Enter a valid choice!!!!!!!!!!!!!!!!")       
    quit=input("If you want the bill y/n:").lower()
    if quit=="y":
        False
        break
    else:
        continue

print("----------------BILL----------------------") 

for item,price in cart:
    print(f"{item}:${price}")  
print(f"sujal your totalcost is :${total_cost}")     