from turtle import Turtle, Screen

import pandas
from score import Score

pointer = Turtle()
screen = Screen()

screen.bgpic("blank_states_img.gif")
Score()

# asking the user to guess
user_choice = screen.textinput(title="Enter the state ", prompt="What another state's name?")
# datas
datas = pandas.read_csv("50_states.csv")
if user_choice in datas["state"].tolist():
	state_name = datas[datas["state"] == user_choice]["state"]
	print(state_name)
else:
	print("there is no state with this name")

screen.mainloop()
screen.exitonclick()
