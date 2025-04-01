import time
from turtle import Turtle, Screen
from Snake import Snake
from Food import Food
from Scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('green')
screen.title('Snake Arcade')
turtles = []
END_OF_GAME = False

screen.tracer(0)

# TODO 1 : Create a Snake body
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

screen.update()
while not END_OF_GAME:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Collision with Wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset_game()
        score.reset()
    # Collision with own tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset_game()
            score.reset()
    # Collision with food
    if snake.head.distance(food) < 20:
        food.generate_food()
        score.increase_score()
        snake.add_new_segment()
screen.exitonclick()
