import art
import game_data
import random
import os

#Shows the logo at the beginning of the game
print(art.logo)

#Conditional for keep the game
answer_is_right = True

#Keep the score of the player
score = 0

#Randomly chooses an accounts from the data
first_account = random.choice(game_data.data)

while answer_is_right:
    second_account = random.choice(game_data.data)

    #Gives some information about the accounts
    print(f"Compare A: {first_account['name']}, a {first_account['description']}, from {first_account['country']}.")
    print(art.vs)
    print(f"Against B: {second_account['name']}, a {second_account['description']}, from {second_account['country']}.")

    #User chooses who they think have more followers
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()

    #Compare the two accounts to see if the player is right and add score
    if user_choice == "a" and first_account["follower_count"] > second_account["follower_count"]:
        score += 1
        os.system('cls')
        print(art.logo)
        print(f"You're right! Current score: {score}")
    elif user_choice == "b" and second_account["follower_count"] > first_account["follower_count"]:
        score += 1
        first_account = second_account
        os.system('cls')
        print(art.logo)
        print(f"You're right! Current score: {score} ")
    else:
        os.system('cls')
        print(art.logo)
        print(f"Sorry, that's wrong. Final score: {score}")
        answer_is_right = False