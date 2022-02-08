import random
def game(comp,you):
    if   comp=="R" and you=="P":
        return True
    elif comp=="R" and you=="S":
        return False
    elif comp=="R" and you=="R":
        return None
    elif comp=="P" and you=="S":
        return True
    elif comp=="P" and you=="R":
        return False
    elif comp=="P" and you=="P":
        return None
    elif comp=="S" and you=="R":
        return True
    elif comp=="S" and you=="P":
        return False
    elif comp=="S" and you=="S":
        return None
t=int(input("Enter the no. of times you want to play \n"))
count =0
T=t
while t!=0:
    c=random.randint(1,3)
    if c==1:
        comp="R"
    elif c==2:
        comp="P"
    elif c==3:
        comp ="S"
    print("Computer has choosen, it's your turn. ")
    you=input("Enter your choice : Rock(R), Paper(P), Scissor(S) \n")
    print("Computer choose ",comp ,"| You choose ",you)
    if game(comp,you)==None:    
        print("It's a tie :| ")
        count += 1
    elif game(comp,you)==True:
        print("You win :) ")
        count += 2
    elif game(comp,you)==False:
        print("You lose :( ")
    t -= 1
print("Your score is ", count,"/",T*2)
