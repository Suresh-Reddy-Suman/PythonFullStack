import random
import colorgram
from turtle import Turtle as t, Screen as s

colors = colorgram.extract("varudu_pic.jpg", 20)

main_color = []
for color in range(0, len(colors)):
    r = colors[color].rgb.r
    g = colors[color].rgb.b
    b = colors[color].rgb.b
    new_color = (r, g, b)
    main_color.append(new_color)

print(random.choice(main_color))

bunny = t()
screen = s()
screen.colormode(255)
bunny.speed(10)

print(screen.canvheight)
print(screen.canvwidth)

X_COR = -380
Y_COR = -280

bunny.penup()
bunny.setposition(-380, -280)
for value in range(9):
    for values in range(10):
        bunny.dot(30)
        bunny.color(random.choice(main_color))
        bunny.forward(80)
    bunny.setposition(X_COR, bunny.ycor() + 80)

bunny.setposition(X_COR,Y_COR)

screen.exitonclick()
