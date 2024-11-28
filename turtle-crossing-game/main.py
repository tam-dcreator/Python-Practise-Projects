import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()


screen.onkey(fun=player.move, key="Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_level()
    for cars in car_manager.cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
