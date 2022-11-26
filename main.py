from turtle import Turtle, Screen

import pandas

from score import Score

pointer = Turtle()
pointer.penup()
screen = Screen()

screen.bgpic("blank_states_img.gif")
score = Score()

# datas
datas = pandas.read_csv("50_states.csv")
all_states = datas["state"].tolist()
correct_states = []
missed_states = []

while len(correct_states) < 50:
    # asking the user to guess
    user_choice = screen.textinput(title="Enter the state ", prompt="What another state's name?").title()
    if user_choice == "Exit":
        for state in all_states:
            if state not in correct_states:
                missed_states.append(state)
        learn_states_table = pandas.DataFrame(missed_states)
        learn_states_table.to_csv("states_to_learn.csv")
        break
    if user_choice in all_states:
        state_name = datas[datas["state"] == user_choice]["state"]
        xcor = datas[datas["state"] == user_choice]["x"]
        ycor = datas[datas["state"] == user_choice]["y"]

        # creating turtle to detect and pin states
        text = Turtle()
        text.color("black")
        text.hideturtle()
        text.penup()
        text.speed(0)
        text.goto(int(xcor), int(ycor))
        pointer.goto(int(xcor), int(ycor))
        text.write(state_name.item(), font=("Arial", 10, "normal"))

        # score = Turtle()
        # score.color("black")
        # score.penup()
        # score.goto(-60, 270)
        print(state_name)
        correct_states.append(user_choice)
    else:
        print("there is no state with this name")

screen.mainloop()
