import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE

    def create_cars(self):
        random_value = random.randint(1, 6)
        if random_value == 6:
            new_car = Turtle(shape='square')
            new_car.penup()
            new_car.color(random.choice(COLORS))
            y_value = random.randint(-250, 280)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.goto(-300, y_value)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.carspeed)

    def update_level(self):
        self.carspeed +=MOVE_INCREMENT
