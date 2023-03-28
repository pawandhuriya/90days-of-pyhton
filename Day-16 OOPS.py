# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("red")
# timmy.forward(100)
#
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

# ---------------python package---------------------
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon name ",["Pikachu","squral","charmandl"])
table.add_column("Type",["Electric","water","fire"])

print(table)
