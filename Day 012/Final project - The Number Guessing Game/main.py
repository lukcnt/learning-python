import art
import random

def game(attempts, secret_number):
    while attempts > 0:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == secret_number:
            print("Spot on, YOU WIN!!!")
            exit()
        elif guess > secret_number:
            attempts -= 1
            print("Too high.")
        else:
            attempts -= 1
            print("Too low.")
        if attempts > 0:
            print("Guess again.")
        else:
            print("You've run out of guesses, you lose.")

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty, Type 'easy' or 'hard': ").lower()

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("That's not a option.")
    exit()

secret_number = random.randint(1,100)

game(attempts, secret_number)

