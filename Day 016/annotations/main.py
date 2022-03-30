import turtle
roberto = turtle.Turtle()

from turtle import Turtle, Screen

roberto = Turtle()
print(roberto)
roberto.shape("turtle")
roberto.color("darkcyan")
roberto.forward(100)
roberto.left(50)
roberto.forward(100)
roberto.left(50)
roberto.forward(100)
roberto.left(50)
roberto.forward(100)
roberto.left(50)
roberto.forward(100)
roberto.left(50)
roberto.forward(100)
roberto.left(50)
roberto.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table)
