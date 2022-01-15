import random

mine = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
mineInteger = int(mine)
oponent = random.randint(0, 2)

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


if mineInteger == 0 and oponent == 2:
  print(f"{rock}\nComputer choose:\n{scissors}\nYou win!!!")
elif mineInteger == 0 and oponent == 1:
  print(f"{rock}\nComputer choose:\n{paper}\nYou lose!")
elif mineInteger == 0 and oponent == 0:
  print(f"{rock}\nComputer choose:\n{rock}\nIt's a draw!!")
elif mineInteger == 1 and oponent == 0:
  print(f"{paper}\nComputer choose:\n{rock}\nYou win!!!")
elif mineInteger == 1 and oponent == 2:
  print(f"{paper}\nComputer choose:\n{scissors}\nYou lose!")
elif mineInteger == 1 and oponent == 1:
  print(f"{paper}\nComputer choose:\n{paper}\nIt's a draw!!")
elif mineInteger == 2 and oponent == 1:
  print(f"{scissors}\nComputer choose:\n{paper}\nYou win!!!")
elif mineInteger == 2 and oponent == 0:
  print(f"{scissors}\nComputer choose:\n{rock}\nYou lose!")
elif mineInteger == 2 and oponent == 2:
  print(f"{scissors}\nComputer choose:\n{scissors}\nIt's a draw!!")
else:
  print("The chosen number isn't valid.")