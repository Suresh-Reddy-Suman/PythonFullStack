import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(0.5)
        self.color('blue')
        self.generate_food()

    def generate_food(self):
        x_cor = random.randint(-280,280)
        y_cor = random.randint(-280,280)
        self.goto(x_cor,y_cor)