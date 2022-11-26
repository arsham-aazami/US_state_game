from turtle import Turtle, Screen
import pandas
from score import Score

pointer = Turtle()
pointer.penup()
screen = Screen()

screen.bgpic("blank_states_img.gif")
score = Score()

# asking the user to guess

# datas
datas = pandas.read_csv("50_states.csv")
all_states = datas["state"].tolist()

correct_guess = 0
while correct_guess < 50:
    user_choice = screen.textinput(title="Enter the state ", prompt="What another state's name?").title()
    if user_choice in all_states:
        state_name = datas[datas["state"] == user_choice]["state"]
        xcor = datas[datas["state"] == user_choice]["x"]
        ycor = datas[datas["state"] == user_choice]["y"]
        text = Turtle()
        text.color("black")
        text.hideturtle()
        text.penup()
        text.speed(0)
        text.goto(int(xcor), int(ycor))
        pointer.goto(int(xcor), int(ycor))
        text.write(state_name.item(), font=("Arial", 10, "normal"))
        print(state_name)
    else:
        print("there is no state with this name")

    correct_guess += 1

screen.mainloop()
