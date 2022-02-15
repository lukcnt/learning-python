import data


def report():
    """ Shows how much of the ingredients and money the coffee machine have"""
    for supplies in data.resources:
        if supplies == "water" or supplies == "milk":
            print(f"{supplies.title()}: {data.resources[supplies]}ml")
        elif supplies == "coffee":
            print(f"{supplies.title()}: {data.resources[supplies]}g")
        else:
            print(f"{supplies.title()}: ${data.resources[supplies]}")


# Keep attending after finishing an order
next_customer = True

while next_customer:
    # Gives the options for the customer order
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "espresso" or order == "latte" or order == "cappuccino":
        print(order)

    # Turn the coffee machine off
    elif order == "off":
        print("The coffee machine will be turned off.")
        next_customer = False

    # Print the resources
    elif order == "report":
        report()

    else:
        print("This isn't a option, please select a option from the menu.")