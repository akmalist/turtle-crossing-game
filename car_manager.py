import random
from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 6:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=0.8, stretch_len=1.5)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = randint(-250, 250)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT




    # def random_cars(self):
    #     new_x = self.xcor() + randint(-350, 350)
    #     new_y = self.ycor() + randint(-350, 350)
    #     self.car((new_x, new_y))

    # for each_turtle in range(0, 30):
    #     new_turtle = Turtle('square')
    #     new_turtle.penup()
    #     new_turtle.shapesize(stretch_wid=0.8, stretch_len=1.5)
    #     new_x = new_turtle.xcor() + randint(-350, 350)
    #     new_y = new_turtle.ycor() + randint(-350, 350)
    #     new_turtle.goto(new_x, new_y)
    #     all_turtles.append(new_turtle)
    #
    # for each_turtle in all_turtles:
    #         each_turtle.backward(10)
