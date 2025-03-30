from turtle import Turtle

POSITIONS = [(-60, 200), (20, 200)]


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto(POSITIONS[0])
        self.write(self.l_score, font=('Courier', 40, 'bold'))
        self.goto(POSITIONS[1])
        self.write(self.r_score, font=('Courier', 40, 'bold'))
        self.dashed_line()

    def dashed_line(self):
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        for line in range(30):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()

    def update_score(self):
        self.clear()
        self.dashed_line()
        self.penup()
        self.goto(POSITIONS[0])
        self.write(self.l_score, font=('Courier', 40, 'bold'))
        self.goto(POSITIONS[1])
        self.write(self.r_score, font=('Courier', 40, 'bold'))

    def left_score(self):
        self.l_score += 1
        self.update_score()

    def right_score(self):
        self.r_score += 1
        self.update_score()
