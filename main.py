from turtle import Turtle, Screen

import pandas
from score import Score

pointer = Turtle()
screen = Screen()

screen.bgpic("blank_states_img.gif")
Score()

# asking the user to guess
# Input(input("Enter state: "))

# datas
datas = pandas.read_csv("50_states.csv")

screen.mainloop()
screen.exitonclick()
