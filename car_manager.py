COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_speed=STARTING_MOVE_DISTANCE
        # 300 random.randint(-230,230)
        # self.forward(100)
        # new_cars.initial_speed = self.car_speed

    def create_cars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_cars = Turtle()
            new_cars.shape('square')
            new_cars.penup()
            new_cars.color(random.choice(COLORS))
            new_cars.shapesize(stretch_wid=1, stretch_len=2)
            # new_cars.initial_speed = self.car_speed
            new_cars.setheading(180)
            new_cars.goto(300, random.randint(-230, 230))
            self.all_cars.append(new_cars)

    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed+=MOVE_INCREMENT


