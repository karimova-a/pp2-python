import random

def guess():
    to_guess = random.randint(1,20)
    
    name = input("Hello! What is your name?")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    attempts = 0
    while True:
        inp = int(input("Take a guess."))
        attempts += 1

        if inp < to_guess:
            print("Your guess is too low.")
        elif inp > to_guess:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
            break  

        
guess()
