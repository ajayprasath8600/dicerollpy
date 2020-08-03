import random
def diceroll(n): 
    if n==1:
        print("o")
        print("Repeat again")
    if n==2:
        print("o ")
        print(" o")
    if n==3:
        print("o  ")
        print(" o ")
        print("  o")
    if n==4:
        print("o o")
        print("o o")
    if n==5:
        print("o o")
        print(" o ")
        print("o o")
    if n==6:
        print("o o")
        print("o o")
        print("o o")
        print("Repeat again")
print("The Dice Roll Game")
c=input("Enter space to start")
f=True
if(c==" "):
    diceroll(random.randint(1,7))
while(f):
    rr=input("Do you want to continue?(y/n)")
    if(rr=='y' or rr=='Y'):
        diceroll(random.randint(1,7))
    elif(rr=='n' or rr=='N'):
        print("Thank you for rolling")
        f=False
    else:
        print("OOPS!!Seems you have entered wrong choice")
