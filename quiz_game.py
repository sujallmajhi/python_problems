questions=("1.Biggest planet in our solar system:","2.Which is mamal among these:","3:fastest Animal on earth:","4.Biggest Mammal on earth:")
options=(("A.Earth","B.Mercury","C.Jupiter","D.pluto"),("A.Goat","B.Chicken","C.Crow","D.Eagle"),("A.Cheetah","B.Tiger","C.Lion","D.Leopard"),("A.Elephant","B.Blue whale","C.Giraffe","D.Platypus"))
answers=("C","A","A","B")
guesses=[]
score=0
question_num=0

guesses=[]
for question in questions:
    print("-------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("Enter A,B,C,D::").upper()
    guesses.append(guess)
    if guess==answers[question_num]:
            score+=1
            print("Correct Answer")
    else:
        print("Incorrect answer")
        print(f"{answers[question_num]}is the correct") 
          
    question_num+=1
print(f"your score is:{score}")    