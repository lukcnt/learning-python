print("Welcome to the tip calculator!")
price = input("What was the total bill? $")
tip = input("How much tip would you like to give? 10, 12, or 15? ")
people = input("How many people to split the bill? ")

tipTotal = float(price) * (int(tip) / 100)
priceTotal = float(price) + tipTotal
pricePerson = '{:.2f}'.format(round(priceTotal / int(people), 2))
print(f"Each person should pay: ${pricePerson}")