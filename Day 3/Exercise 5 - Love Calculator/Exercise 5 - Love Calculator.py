print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

names = name1.lower() + name2.lower()

letterT = names.count("t")
letterR = names.count("r")
letterU = names.count("u")
letterE = names.count("e")
true = letterT + letterR + letterU + letterE

letterL = names.count("l")
letterO = names.count("o")
letterV = names.count("v")
letterE = names.count("e")
love = letterL + letterO + letterV + letterE

trueLove = str(true) + str(love)

if int(trueLove) < 10 or int(trueLove) > 90:
  print(f"Your score is {trueLove}, you go together like coke and mentos.")
elif int(trueLove) >= 40 and int(trueLove) <= 50:
  print(f"Your score is {trueLove}, you are alright together.")
else:
  print(f"Your score is {trueLove}.")