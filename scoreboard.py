from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.goto(-210, 265)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"LEVEL = {self.score}", align='center', font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER\n YOUR SCORE = {self.score}", align='center', font=FONT)