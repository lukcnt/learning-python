import art
import os

print(art.logo)

def auction():
    auctionData = {}
    moreBidders = True
    while moreBidders:
        name = input("What is your name? : ")
        bid = int(input("What's your bid? : $"))
        auctionData[name] = bid
        keepGoing = input("Are there any other bidders? Type 'yes' or 'no'\n")
        if keepGoing == "no":
            moreBidders = False
        os.system('cls')
    winner = max(auctionData, key=auctionData.get)
    amount = max(auctionData.values())
    print(f"The winner is {winner} with a bid of ${amount}.")

auction()