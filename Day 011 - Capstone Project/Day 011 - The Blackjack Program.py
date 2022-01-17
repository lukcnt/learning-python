############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10}]

start = input("Do you want to play a game of Blackjack? Type 'yes' or 'no': ")
if start == "yes":
    print(art.logo)
else:
    exit()