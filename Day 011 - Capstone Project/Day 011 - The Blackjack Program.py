import art
import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
userCards = []
computerCards = []

#Draw a random card from the list "cards".
def draw():
    card = random.choice(cards)
    return card

#Shows the players' hands during the game.
def informationPartial():
    print(f"Your cards: {userCards}, current score: {sum(userCards)}")
    print(f"Computer's first card: {computerCards}")

#Shows the final hand of the players and final score.
def informationFinal():
    print(f"Your final hand: {userCards}, final score: {sum(userCards)}")
    print(f"Computer's final hand: {computerCards}, final score: {sum(computerCards)}")

#Transforms the ace into the best card for the player.
def ace():
    if (sum(userCards)) > 21 and 11 in userCards:
        position = userCards.index(11)
        userCards[position] = 1

#Compare the scores to determine whether it was a win, loss, or draw.
def compare():
    if (sum(userCards)) == (sum(computerCards)):
        informationFinal()
        print("It's a draw! \U0001F610")
    elif (sum(userCards)) > (sum(computerCards)) or (sum(computerCards)) > 21:
        informationFinal()
        print("You WIN! \U0001F600")
    else:
        informationFinal()
        print("Computer win, you lose! \U0001F62D")

#Blackjack game.
def game():
    #Give the initial cards.
    for card in range(2):
        userCards.append(draw())
    computerCards.append(draw())
    informationPartial()

    #It keeps dealing cards as long as the player wants.
    moreCards = True
    while moreCards:
        if (sum(userCards)) == 21:
            moreCards = False
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
            if choice == "y":
                userCards.append(draw())
                ace()
                informationPartial()
                if (sum(userCards)) >= 21:
                    moreCards = False
            else:
                moreCards = False

    #Compare the hands and show the result.
    if (sum(userCards)) == 21:
        computerCards.append(draw())
        informationFinal()
        if (sum(userCards)) == (sum(computerCards)):
            print("It's a draw! \U0001F610")
        else:
            print("Blackjack, YOU WIN! \U0001F60E")
    elif (sum(userCards)) > 21:
        computerCards.append(draw())
        informationFinal()
        print("You went over, you lose! \U0001F641")
    else:
        while (sum(computerCards)) < 17:
            computerCards.append(draw())
            ace()
        compare()

    #Gives the option to keep playing the game.
    keepPlaying = input("Do you want to play another game of Blackjack? Type 'yes' or 'no': ")
    if keepPlaying == "yes":
        os.system("cls")
        userCards.clear()
        computerCards.clear()
        game()
    else:
        exit()

#Menu og the game.
start = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")
if start == "yes":
    print(art.logo)
    game()
else:
    exit()