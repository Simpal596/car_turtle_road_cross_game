from turtle import Turtle
from random import choice, randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.car = []

    def car_making(self):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.shapesize(stretch_wid=1, stretch_len=2)
        new_turtle.setheading(180)
        new_turtle.color(choice(COLORS))
        new_turtle.penup()
        y_cor = randint(-280, 260)
        new_turtle.goto(280, y_cor)
        self.car.append(new_turtle)

    def car_move(self):
        for item in self.car:
            item.forward(STARTING_MOVE_DISTANCE)

    def increment(self):
        global STARTING_MOVE_DISTANCE, MOVE_INCREMENT
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
