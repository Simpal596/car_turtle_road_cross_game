from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.refresh_player()
        self.level = 1

    def move(self):
        self.fd(MOVE_DISTANCE)

    def level_up(self):
        if self.ycor() > FINISH_LINE_Y:
            self.level += 1

    def player_finish(self):
        if self.ycor() == FINISH_LINE_Y:
            return True

    def refresh_player(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

