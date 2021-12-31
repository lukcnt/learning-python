age = input("What is your current age? ")

lifeExpectancy = 90
days = 365
weeks = 52
months = 12

daysLeft = (lifeExpectancy - int(age)) * days
weeksLeft = (lifeExpectancy - int(age)) * weeks
monthsLeft = (lifeExpectancy - int(age)) * months

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")


