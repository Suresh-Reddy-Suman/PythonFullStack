from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(220, 200)
        self.score = 0
        self.total_score = 50
        self.write(f"Countries :{self.score}/{self.total_score}", font=('Courier', 10, 'bold'))

    def update_score(self):
        self.score +=1
        self.clear()
        self.write(f"Countries :{self.score}/{self.total_score}", font=('Courier', 10, 'bold'))