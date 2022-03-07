import random
def file(count):
    with open("Hiscore.txt","r") as f:
        hiscore=f.read()
        if int(hiscore)<count:
            with open("Hiscore.txt","w") as f:
                f.write(str(count))
def game(comp,you):
    if   comp=="R" and (you=="P" or you=="p"):
        return True
    elif comp=="R" and (you=="S" or you=="s"):
        return False
    elif comp=="R" and (you=="R" or you=="r"):
        return None
    elif comp=="P" and (you=="S" or you =="s"):
        return True
    elif comp=="P" and (you=="R" or you =="r"):
        return False
    elif comp=="P" and (you=="P" or you =="p"):
        return None
    elif comp=="S" and (you=="R" or you =="r"):
        return True
    elif comp=="S" and (you=="P" or you =="p"):
        return False
    elif comp=="S" and (you=="S" or you =="s"):
        return None
    else:
        return 2
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
    else:
        print("Please enter a valid character")
        t +=1
    t -= 1
print("Your score is ", count,"/",T*2)
file(count) #to store high score in the Hiscore.txt file