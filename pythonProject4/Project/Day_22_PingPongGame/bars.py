from turtle import Turtle

POSITIONS = [(-380, 0), (380, 0)]


class Bar(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.bars = []
        self.generate_bar()
        self.left_bar = self.bars[0]
        self.right_bar = self.bars[1]

    def generate_bar(self):
        for box in POSITIONS:
            new_turtle = Turtle(shape='square')
            new_turtle.color('black')
            new_turtle.setheading(90)
            new_turtle.shapesize(stretch_wid=1, stretch_len=4)
            new_turtle.penup()
            new_turtle.goto(box)
            self.bars.append(new_turtle)

    def up(self):
        if self.left_bar.ycor() < 250:
            self.left_bar.forward(20)

    def down(self):
        if self.left_bar.ycor() > -250:
            self.left_bar.backward(20)

    def move_up(self):
        if self.right_bar.ycor() < 250:
            self.right_bar.forward(20)

    def move_down(self):
        if self.right_bar.ycor() > -250:
            self.right_bar.backward(20)
