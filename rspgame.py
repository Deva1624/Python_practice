import random as rm
import sys

wel = input('Welcome to the Game Do you Want Play type y/n ')

def gameplay():

    print("you have Enter the game Successfully")
    print("paper,scissor,rock")
    inp = input("Pleace type your choice in small letter")
    ch1 = inp
    print(ch1)
    ch2 = rm.choice(["paper","scissor","rock"])
    print(ch2)

    if ch1 == "paper" and ch2 == "rock" or ch1 == "scissor" and ch2 == "paper" or ch1 == "rock" and ch2 == "scissor":
        print("!!!Congartz you have won Choice is: ",ch1)
        print("You Defeated the Bot choice is",ch2)

    elif ch2 == "paper" and ch1 == "rock" or ch2 == "scissor" and ch1 == "paper" or ch2 == "rock" and ch1 == "scissor":
        print("!!!Sorry the bot defeated you", ch2)
        print("Better Luck Next Time your choice is", ch1)
    else:
        print('The Match is tied!!')

    wel1 = input('Do you Want to continue to Play type y/n ')
    if wel1 == 'n':
        sys.exit(0)

n = 1
while n>0:
    if wel == 'y':
        gameplay()
    else:
        print("see you again")
        break