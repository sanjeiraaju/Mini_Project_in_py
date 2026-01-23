questions=("name",
          "class",
          "job")

options=('a.sandy','b.ram','c.quint',
        'a.alony','b.xamy','c.king',
        '.max','b.beta','c.inko')
answers=("c","a",'b')
guesses=[]
score=0
question_num=0

for question in  questions:
    print("-----------")
    print(question,end='')
    for option in options[question_num]:
        print(option)

    guess=input("Enter(a,b,c):").lower()
    guesses.append(guess)

    if guess == answers[question_num]:
        score+=1
        print('correct')
    else:
        print("incorrect")
        print(f"{answers[question_num]} is right")
    question_num+=1
    
    