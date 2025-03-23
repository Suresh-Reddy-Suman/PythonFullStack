from turtle import Turtle as Tim, Screen as S

bunny = Tim()
screen = S()


def move_forward():
    """This method is used to move forward"""
    bunny.forward(10)


def turn_left():
    """This method is used to turn the turtle by 15degrees towards left"""
    bunny.left(15)


def turn_right():
    """This method is used to turn the turtle by 15degrees towards right"""
    bunny.right(15)


def move_backward():
    """This method is used to move backward"""
    bunny.backward(10)


screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key='Down', fun=move_backward)
screen.onkey(key='Right', fun=turn_right)
screen.onkey(key='Left', fun=turn_left)

screen.exitonclick()
