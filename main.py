from random import randint
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
score = Scoreboard()


screen.listen()
screen.onkey(fun=player.move, key="Up")

game_is_on = True

while game_is_on:
    check = randint(0, 6)
    time.sleep(0.1)
    screen.update()
    if check == 6:
        car.car_making()
    car.car_move()
    if player.player_finish():
        score.update_score()
        player.refresh_player()
        car.increment()
    for item in car.car:
        if item.distance(player.position()) <= 20:
            score.game_over()
            game_is_on = False

screen.exitonclick()
