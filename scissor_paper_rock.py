import random
option=("scissor","paper","rock")
name=input("Enter your name:::")
while True:
    player=None
    computer=random.choice(option)
    while player not in option:
        player=input(f"{name}:Enter:scissor,paper,rock::")
    print(f"player={player}")  
    print(f"computer={computer}")  
    if player==computer:
        print("Its a tie game!!!!!!!!!!!")
    elif player=="scissor" and computer=="paper":
        print("you are winner")    
    elif player=="rock"and computer=="scissor":
        print("You are winner!!!!!!!")  
    elif player=="paper" and computer=="rock":
        print("you are winner!!!!!!!!!!")    
    else:
        print("computer is winner")    
    quit=input("if you want to quit y/n").lower()    
    if quit=='y':
        False
        break
print(f"{name}::thanks for playing")    