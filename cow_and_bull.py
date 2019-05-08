# Rules for this game is if you guess the correct number in correct palce then you win..
# Hint: The cows shows how many correct number in correct place and the bulls shows how many correct number in wrong place

import random
import string



numbers = string.digits
lis = [random.choice(numbers) for i in range(4)]
count = 1

def gameplay(en_num,cow,bulls):


    if lis[0] == en_num[0]:
        cow +=1
    if lis[0] != en_num[0] and lis[0] in en_num:
        bulls +=1
    if lis[1] == en_num[1]:
        cow +=1
    if lis[1] != en_num[1] and lis[1] in en_num:
        bulls +=1
    if lis[2] == en_num[2]:
        cow +=1
    if lis[2] != en_num[2] and lis[2] in en_num:
        bulls +=1
    if lis[3] == en_num[3]:
        cow +=1
    if lis[3] != en_num[3] and lis[3] in en_num:
        bulls +=1

    return print("cow" + str(cow) + " " + "Bull" + str(bulls))

if __name__ == '__main__':
    cow = 0
    bulls = 0
    while True:
        inp = input("Guess the Four digits From 0 to 9")
        en_num = [x for x in inp]
        if lis == en_num:
            if count == 1:
                print("!!!!!Extraordinary you Guessed It First Try")
            else:
                print("You Guessed It!!! \n Total Tries You Have Taken is :",count)
            break
        else:
            count +=1
            gameplay(en_num,cow,bulls)
