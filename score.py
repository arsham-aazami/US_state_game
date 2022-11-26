from turtle import Turtle


class Score:
	def __init__(self):
		self.score = 1
		self.total_score = 50
		self.create_score()

	def create_score(self):
		score = Turtle()
		score.color("black")
		score.penup()
		score.speed(0)
		score.hideturtle()
		score.goto(230, 270)
		score.write(f"score: {self.score} / {self.total_score}", font=("Arial", 18, "normal"))

	def increment_score(self):
		self.score += 1
		if self.score == 50:
			self.score = 1
