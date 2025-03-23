# from turtle import Turtle, Screen
#
# bunny = Turtle()
# bunny.shape('turtle')
# bunny.color('red')
#
# # TODO 1 : Draw a Square
# for _ in range(4):
#     bunny.forward(100)
#     bunny.left(90)
#
# my_screen = Screen()
# my_screen.exitonclick()
import random
import turtle
# TODO 2 : Basic Import
# import turtle
#
# tim = turtle.Turtle()

# TODO 3 : From...Import..
# from turtle import Turtle
#
# tim = Turtle()

# TODO 4 : ALIAS
# from turtle import Turtle as Tim
#
# timmy = Tim

# TODO 5: Dashed Line
# from turtle import Turtle as Tim, Screen as Sc
#
# bunny = Tim()
# for _ in range(30):
#     bunny.forward(10)
#     bunny.penup()
#     bunny.forward(10)
#     bunny.pendown()
#
# screen = Sc()
# screen.exitonclick()

# TODO 6: Draw Multiple shape from 3 to 10
# from turtle import Turtle as Tim, Screen as Sc
#
# bunny = Tim()
# screen = Sc()
#
# bunny.width(20)
# screen.colormode(255)
# for side in range(3, 11):
#     angle = 360 / side
#     bunny.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     for shape in range(side):
#         bunny.forward(100)
#         bunny.left(angle)

# bunny.speed(7)
# TODO 7 : DO A RANDOME WALK
# for _ in range(100):
#     bunny.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     bunny.forward(40)
#     bunny.setheading(random.choice([0,90, 180, 270]))
#
#
# screen.exitonclick()

### Tuples ###
# color_palete = (1,4,5)
# print(type(color_palete))
# print(color_palete[2])

### Draw a spyrograph
from turtle import Turtle as Tim, Screen as Sc

bunny = Tim()
screen = Sc()
screen.colormode(255)
bunny.speed(100)

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        bunny.pencolor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        bunny.circle(100)
        bunny.setheading(bunny.heading()+size_of_gap)

draw_spirograph(5)
screen.exitonclick()

