from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.score = 0
        with open("highscore.txt") as get_score:
            self.high_score = int(get_score.read())
        self.write(f"Score: {self.score} High Score : {self.high_score}", font=("Arial", 10, 'bold'))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", font=("Arial", 10, 'bold'))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode='w') as update_score:
                update_score.write(str(self.high_score))

        self.score = 0
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", font=("Arial", 10, 'bold'))
