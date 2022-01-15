print('''
<|
           A             
          /.\       
     <|  [""M#      
      A   | #              
     /.\ [""M#             
    [""M# | #  U"U#U                 
     | #  | #  \ .:/    
     | #  | #___| #     
     | "--'     .-"     
   |"-"-"-"-"-#-#-##    
   |     # ## ######     
    \       .::::'/     
     \      ::::'/      
   :8a|    # # ##      
   ::88a      ###       
  ::::888a  8a ##::.    
  ::::::888a88a[]::::
 :::::::::SUNDOGa8a::::. ..              
 :::::8::::888:Y8888:::::::::...      
::':::88::::888::Y88a______________________________________________________
:: ::::88a::::88a:Y88a                                  __---__-- __
' .: ::Y88a:::::8a:Y88a                            __----_-- -------_-__
  :' ::::8P::::::::::88aa.                   _ _- --  --_ --- __  --- __--
.::  :::::::::::::::::::Y88as88a...s88aa.
''')

print("Welcome to Hogwarts School of Witchcraft and Wizardry .")
print("Your mission is to reach in Gryffindor Tower")

choice1 = input('You\'re at the Great Hall. Where do you want to go? Type "stairs" or "corridor" ')
if choice1.lower() == "stairs":
  choice2 = input('You were walking up the stairs when they start moving. What you gonna do? Type "jump" or "stay" ')
  if choice2.lower() == "jump":
    choice3 = input('You found it!!!!! Now you need the password to access the common room. Choose one of the three "Fortuna Major", "Abracadabra", "Wingardium Leviosa" ')
    if choice3.lower() == "fortuna major":
      print("You did it, got it right. Now have full access to the common room and dormitories of Gryffindor. You WIN!!!!")
    elif choice3.lower() == "abracadabra":
      print("The guardian got scared and thought that you were trying to kill him, you got suspended. Game Over.")
    elif choice3.lower() == "wingardium leviosa":
      print("You got yelled at for using a spell on the guardian. Game Over")
    else:
      print("That's not a option. Game Over.")
  elif choice2.lower() == "stay":
    print("You ended up in the dungeon, got attacked by a troll and died.. Game Over")
  else:
    print("That's not a option. Game Over")
elif choice1.lower() == "corridor":
  print("You got lost in the castle. Game Over")
else:
  print("That's not a option. Game Over.")