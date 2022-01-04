import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

names_quantity = len(names) - 1
the_chosen_one_number = random.randint(0, names_quantity)
the_chosen_one_name = names[the_chosen_one_number]
print(f"{the_chosen_one_name} is going to buy the meal today!")