import random
from turtle import Turtle as Tim, Screen as screen

COLORS = ['red', 'green', 'blue', 'orange', 'brown', 'yellow']
GAME_OVER = False
X_COR = -225
Y_COR = -170
turtles = []
my_screen = screen()

# Set width 500 X height 400
my_screen.setup(width=500, height=400)

# Ask the user his choice
winner = my_screen.textinput('Winner of the race', "Who is going to win the race??")

# Ask timmy to go to start line
for color in COLORS:
    timmy = Tim(shape='turtle')
    timmy.color(color)
    timmy.shapesize(1.3)
    turtles.append(timmy)
    timmy.penup()
    timmy.goto(X_COR, Y_COR)
    Y_COR += 70

while not GAME_OVER:
    new_turtle = random.choice(turtles)
    new_turtle.forward(10)
    if new_turtle.xcor() > 230:
        if new_turtle.color()[0] == winner:
            print("You Won the Game")
        else:
            print(f"You Lose and the winner is {new_turtle.color()[0]}")
        GAME_OVER = True

my_screen.exitonclick()

