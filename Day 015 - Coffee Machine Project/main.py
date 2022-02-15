
# Keep attending after finishing an order
next_customer = True

while next_customer:
    # Gives the options for the customer order
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "espresso" or order == "latte" or order == "cappuccino":
        print(order)
    elif order == "off":
        print("The coffee machine will be turned off.")
        next_customer = False
