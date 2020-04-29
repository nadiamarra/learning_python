while True:
    try:
        num=int(input("Please enter a number: "))
    except ValueError:
        print("Hey, that's not a number!")
    else:
        print(f"Your number is {num}")
        break
    finally:   #runs no matter what
        print("You can do this!")
print("Game over")
    
    
