#questions 
questions=("1.Biggest planet in our solar system:","2.Which is mamal among these:","3:fastest Animal on earth:","4.Biggest Mammal on earth:")
#options of 2D tupple
options=(("A.Earth","B.Mercury","C.Jupiter","D.pluto"),("A.Goat","B.Chicken","C.Crow","D.Eagle"),("A.Cheetah","B.Tiger","C.Lion","D.Leopard"),("A.Elephant","B.Blue whale","C.Giraffe","D.Platypus"))
# answers of the questions
answers=("C","A","A","B")
#list of guesses
guesses=[]
#score variable set to be zero
score=0
#question num to increase the index
question_num=0


for question in questions:
    print("-------------------")
    print(question)
    #question_num for index 0 and question_num+=1 for displaying option one after one
    for option in options[question_num]:
        print(option)
    guess=input("Enter A,B,C,D::").upper()#takes upper Alphabet only
    #append guess of the user in guesses list
    guesses.append(guess)
    #if guess matches the answer at respective index
    if guess==answers[question_num]:
            score+=1
            print("Correct Answer")
    else:
        print("Incorrect answer")
        print(f"{answers[question_num]}is the correct") 
          
    question_num+=1
print(f"your score is:{score}")    