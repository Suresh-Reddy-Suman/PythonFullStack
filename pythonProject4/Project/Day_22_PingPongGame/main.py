import time
from turtle import Screen
from bars import Bar
from Scoreboard import Scoreboard
from ball import Ball

POSITIONS = [(-280, 0), (280, 0)]
END_OF_GAME = False

my_screen = Screen()
my_screen.listen()
my_screen.title('Welcome to PingPong Game')
my_screen.setup(width=800, height=600)
my_screen.tracer(0)

bar = Bar()
score_board = Scoreboard()
ball = Ball()

my_screen.onkey(key='w', fun=bar.up)
my_screen.onkey(key='s', fun=bar.down)
my_screen.onkey(key='Up', fun=bar.move_up)
my_screen.onkey(key='Down', fun=bar.move_down)
while not END_OF_GAME:
    my_screen.update()
    time.sleep(0.01)
    ball.move()

    # Collision with Wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce()

    if ball.distance(bar.right_bar) < 50 and ball.xcor() > 365:
        ball.bar_bounce()

    if ball.distance(bar.left_bar) < 50 and ball.xcor() < -365:
        ball.bar_bounce()

    if ball.xcor() > 390:
        ball.reset_game()
        score_board.left_score()

    if ball.xcor() < -390:
        ball.reset_game()
        score_board.right_score()

my_screen.exitonclick()
