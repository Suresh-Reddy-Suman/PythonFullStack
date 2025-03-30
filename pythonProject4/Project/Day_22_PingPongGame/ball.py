from turtle import Turtle

X_DISTANCE = 2
Y_DISTANCE = 2


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(0.5)
        self.color('blue')
        self.speed('slow')
        self.x_value = 2
        self.y_value = 2

    def move(self):
        self.goto(self.xcor() + self.x_value, self.ycor() + self.y_value)

    def bounce(self):
        self.y_value *= -1

    def bar_bounce(self):
        self.x_value *= -1
        self.y_value *= 1

    def reset_game(self):
        self.goto(0,0)
        self.x_value *=-1

