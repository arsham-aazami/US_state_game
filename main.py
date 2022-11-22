import turtle
from turtle import Turtle, Screen
from score import Score
import pandas

pointer = Turtle()
screen = Screen()

screen.bgpic("blank_states_img.gif")
Score()


# asking the user to guess
# Input(input("Enter state: "))


# getting the coordinates of a specific state
def state_coordinate(x, y):
	print(x, y)
onclick_coordinate = turtle.onscreenclick(state_coordinate)


# datas
pandas.read_csv("")
screen.mainloop()
screen.exitonclick()
