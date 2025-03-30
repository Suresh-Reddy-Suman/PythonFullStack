import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
s_board = Scoreboard()
car_manager = CarManager()
screen.listen()
screen.onkey(key='Up', fun=player.move_up)
game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    if player.is_at_finish_line():
        s_board.update_score()
        car_manager.update_level()
        player.reset_player()

    # Collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 10:
            s_board.game_over()
            game_is_on = False
