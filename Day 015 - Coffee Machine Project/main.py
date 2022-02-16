import data


def report():
    """ Shows how much of the ingredients and money the coffee machine have."""
    for supplies in data.resources:
        if supplies == "water" or supplies == "milk":
            print(f"{supplies.title()}: {data.resources[supplies]}ml")
        elif supplies == "coffee":
            print(f"{supplies.title()}: {data.resources[supplies]}g")
        else:
            print(f"{supplies.title()}: ${data.resources[supplies]}")


def check_resources(order):
    """ Check if the coffee machine have enough resources to make the order of the customer."""
    for types in data.MENU:
        if order == types:
            for supplies in data.MENU[types]["ingredients"]:
                if data.resources[supplies] >= data.MENU[types]["ingredients"][supplies]:
                    return True
                else:
                    print(f"Sorry there is not enough {supplies}.")
                    return False


def process_coins():
    """ Queries and calculates the monetary value of the coins inserted."""
    print("Please insert coins. ")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How manu pennies?: ")) * 0.01
    client_payment = quarters + dimes + nickles + pennies
    return round(client_payment, 2)


def transaction_successful(payment):
    """ Checks if the user has inserted enough money to purchase the drink they selected."""
    if payment > data.MENU[order]["cost"]:
        change = round(payment - data.MENU[order]["cost"], 2)
        data.resources["money"] += data.MENU[order]["cost"]
        print(f"Here is ${change} dollars in change.")
        return True
    elif payment == data.MENU[order]["cost"]:
        data.resources["money"] += data.MENU[order]["cost"]
        print("No change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(order):
    """ Deduct the ingredients needed to make the customer order from the coffee machine resources."""
    for types in data.MENU:
        if order == types:
            for supplies in data.MENU[types]["ingredients"]:
                data.resources[supplies] -= data.MENU[types]["ingredients"][supplies]
            print(f"Here is your {order} ☕ Enjoy!")


# Keep attending after finishing an order.
next_customer = True

while next_customer:
    # Gives the options for the customer order.
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "espresso" or order == "latte" or order == "cappuccino":
        if check_resources(order):
            payment = process_coins()
            if transaction_successful(payment):
                make_coffee(order)

    # Turn the coffee machine off.
    elif order == "off":
        print("The coffee machine will be turned off.")
        next_customer = False

    # Print the resources
    elif order == "report":
        report()

    else:
        print("This isn't a option, please select an option from the menu.")
#
