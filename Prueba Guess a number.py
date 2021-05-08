print("Try to guess some numbers from 0 to 10. Type \"q\" to quit.") 
numbers = ["1","5","7","9"]
while True:
    a = input()
    if a == "q":
        break
    elif a in numbers:
        print("You guessed.")
    else:
        print("You didn't guess, try again.")
