#Functions
def my_function():
  print("Hello")
  print("Bye")

my_function()

#Reeborg's World
def turn_around():
    turn_left()
    turn_left()

def turn_right():
    turn_left()
    turn_left()
    turn_left()

#Draw Square
turn_left()
move()
turn_right()
move()
turn_right()
move()
turn_right()
move()