from turtle import Turtle


class Input:
	def __init__(self, value):
		self.text = "Enter state :"
		self.value = value
		self.create_input()

	def create_input(self):
		input = Turtle()
		input.color("black")
		input.penup()
		input.speed(0)
		input.hideturtle()
		input.goto(-230, 280)
		input.write(self.text, font=("Arial", 18, "normal"))
