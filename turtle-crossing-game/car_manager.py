from turtle import Turtle
import random as r

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.move_distance = 5
        self.cars = []


    def create_car(self):
        random_chance = r.randint(1, 3)
        if random_chance == 1:
            car = Turtle("square")
            car.color(r.choice(COLORS))
            car.penup()
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.setpos(300, r.randrange(-250, 250, 25))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.seth(180)
            car.fd(self.move_distance)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
