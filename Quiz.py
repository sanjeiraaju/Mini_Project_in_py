question=("how many bones:","what is your name:","what is your mark:","what are your quality","what is your aim")
option=(("A.211","B.212","C.33","D.206"),
        ("A.ramu","B.gabi","C.optm","D.raju"),
        ("A.111","B.412","C.33","D.206"),
        ("A.bad","B.worse","C.good","D.perfect"),
        ("A.salary","B.rich","C.travel","D.interest"))
answer=["D","D","B","D","A"]
guess=[]
score=0
question_num=0
for i in question:
    print(i)
    for j in option[question_num]:
        print(j)
    print()
    a=input("Enter (A,B,C,D):").upper()
    guess.append(a)
    if a==answer[question_num]:
        print("CORRECT")
        score+=1
    else:
        print("INCORRECT")
    question_num+=1
print("------")
print("RESULT")

print("answer",end='')
for ans in answer:
    print(f"{ans}",end='')
print()


print("guess:",end='')
for p in guess:
    print(f"{p}",end='')
print()

scoe=int((score/len(question))*100)
print(f"your score:{scoe}%")