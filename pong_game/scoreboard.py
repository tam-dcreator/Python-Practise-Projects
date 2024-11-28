from turtle import Turtle

FONT = ("courier", 80, "normal")
SCORE_POSITIONS = [(-50, 290), (50, 290)]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.value = 0
        self.l_score = 0
        self.r_score = 0
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=FONT)

    def right_score(self):
        self.r_score += 1
        self.write_score()

    def left_score(self):
        self.l_score += 1
        self.write_score()
