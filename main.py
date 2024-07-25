import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
score = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkey(key='Up', fun=player.move)

game_is_on = True
level=0.1
while game_is_on:
    time.sleep(level)
    screen.update()

    cars.create_cars()
    cars.move_cars()
    #detect collision with the car
    for car in cars.all_cars:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on=False
    if player.winner():
        score.increase_level()
        cars.increase_speed()
screen.exitonclick()
