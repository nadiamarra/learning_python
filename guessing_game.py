import random
random_number=random.randint(1,10)
    
while True:
    msg=input("Guess a number from 1 to 10: ")
    msg=int(msg)
    if msg==random_number:
        print("You won!")
        play_again=input("Play again? (y/n) ")
        if play_again=="y":
            random_number=random.randint(1,10)
            msg=""
        else:
            print("Thanks, bye!")
            break
    elif msg>random_number:
        print("Too high! Guess again")
    else:
        print("Too low! Guess again")     
