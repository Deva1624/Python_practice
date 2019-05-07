import random as rm


print("Welcom to Guessing Game")

def gamepaly():
    correct_choice = 0
    incorrect_choice = 0
    while True:
        user_choice = int(input("Choose Any  Number Between 0 to 9 : "))
        rand_num = rm.randint(0, 10)
        print("The number is :",rand_num)

        if user_choice == rand_num:
            correct_choice = correct_choice+1
            print("You have guessed correctly")

        if user_choice != rand_num:
            if user_choice > rand_num:
                print('sorry too high')
            if user_choice < rand_num:
                print('sorry too low')
            incorrect_choice = incorrect_choice+1
            print("Better Luck Next Time")
        user_choice2 = input("Type exit to Exit the game")
        if user_choice2 == 'exit':
            print('Thanks for Playing Total Correct Choice is :',correct_choice)
            print('Incorrect choices are :',incorrect_choice)
            break
        else:
            continue

gamepaly()