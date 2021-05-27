# 1. A turtle moves forwards when you press the "Up" key. It can only move forwards, not back, left or right.
# 2. Cars are randomly generated along the y-axis and will move from the right edge of the screen to the left edge.

import time
from random import randint
from turtle import Screen

from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

score = Scoreboard()
screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
cars = CarManager()
game_is_on = True
screen.onkey(player.move, "Up")


while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_cars()

    # finished
    if player.finish_line():
        player.go_to_start()
        cars.increase_speed()
        score.increase_point()

    # detect collision with cars
    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False



screen.exitonclick()