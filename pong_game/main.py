from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Pong Game")
screen.setup(height=700, width=1200)
screen.tracer(0)
screen.listen()
l_paddle = Paddle((-580, 0))
r_paddle = Paddle((580, 0))

center_line = Paddle((0, 310))
center_line.hideturtle()
center_line.seth(270)
for _ in range(32):
    center_line.pendown()
    center_line.forward(10)
    center_line.penup()
    center_line.forward(10)

ball = Ball()
scoreboard = Scoreboard()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() == 350 or ball.ycor() == -350:
        ball.bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 560 or ball.distance(l_paddle) < 50 and ball.xcor() < -560:
        ball.bounce_off_paddle()
    if ball.xcor() > 580:
        ball.reset_position()
        scoreboard.left_score()
    if ball.xcor() < -580:
        ball.reset_position()
        scoreboard.right_score()

screen.exitonclick()
