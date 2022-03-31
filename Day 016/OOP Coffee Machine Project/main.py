from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
next_customer = True

while next_customer:
    options = menu.get_items()

    # Gives the options for the customer order.
    order = input(f"What would you like? ({options}): ").lower()

    # Turn the coffee machine off.
    if order == "off":
        print("The coffee machine will be turned off.")
        next_customer = False

    # Print the resources.
    elif order == "report":
        coffee_maker.report()
        money_machine.report()

    # Make the order of the customer.
    else:
        beverage = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(beverage) and money_machine.make_payment(beverage.cost):
            coffee_maker.make_coffee(beverage)
