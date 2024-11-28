from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.right, key="Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.ycor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 1:
            scoreboard.reset_score()
            snake.reset()
screen.exitonclick()
