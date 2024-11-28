from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.setpos(0, 260)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.write_score()

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as d:
                d.write(f"{self.high_score}")
        self.score = 0
        self.write_score()
