from turtle import Turtle


class Location(Turtle):

    def __init__(self, name, x_cor, y_cor):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x_cor, y_cor)
        self.write(name, font=('Courier', 10, 'bold'))



