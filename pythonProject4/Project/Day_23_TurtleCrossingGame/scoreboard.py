from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(x=-290, y=250)
        self.write(f'Score : {self.score}', font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f'Score : {self.score}', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", font=FONT)

