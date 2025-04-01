from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        """This method is used to create a snake body with 3 segments"""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            new_turtle = Turtle(shape='square')
            new_turtle.penup()
            new_turtle.color('white')
            new_turtle.goto(position)
            self.segments.append(new_turtle)

    def move(self):
        """
        This method is used to move the snake
        """
        for segment in range(len(self.segments) - 1, 0, -1):
            self.segments[segment].goto(self.segments[segment - 1].xcor(), self.segments[segment - 1].ycor())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def add_new_segment(self):
        new_turtle = Turtle(shape='square')
        new_turtle.penup()
        new_turtle.color('white')
        self.tail = self.segments[len(self.segments) - 1]
        x_cor = self.tail.xcor()
        y_cor = self.tail.ycor()
        new_turtle.goto((x_cor, y_cor))
        self.segments.append(new_turtle)

    def reset_game(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
