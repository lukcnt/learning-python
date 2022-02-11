#Import the art from the art.py file
import art

#Shows the logo at the beginning of the game
print(art.logo)

# Import the data from game_data.py file
import game_data
import random

#Randomly chooses two accounts from the data
first_account = random.choice(game_data.data)
second_account = random.choice(game_data.data)

#Gives some information about the accounts
print(f"Compare A: {first_account['name']}, a {first_account['description']}, from {first_account['country']}.")
print(art.vs)
print(f"Against B: {second_account['name']}, a {second_account['description']}, from {second_account['country']}.")

## Loop to go through all the data in the data list(desnecessary)
# for information in range(len(data)):
#     print(data[information])

## Shows a specific part of the information in the dictionary
# print(data[0]["name"])
# print(data[0])

## Visual comparision of the data
# print(f"Compare A: {data[0]}.")
# print(vs)
# print(f"Against B: {data[1]}.")

## Choose a random dictionary in the data list
# a = random.choice(data)
# print(a)
# print(type(a))

## Compare if the data choosen is the same
# a = game_data.data[0]
# b = game_data.data[0]
# if a == b:
#     print("True")
# else:
#     print("False")