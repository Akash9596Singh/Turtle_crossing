FONT = ("Courier", 24, "normal")
POSITION = (-270, 250)
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(POSITION)
        self.level = 1
        self.updarte_score()
    def updarte_score(self):
        self.clear()
        self.write(f"Level: {self.level}", move=False, align='left', font=FONT)

    def increase_level(self):
        self.level += 1
        self.updarte_score()
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", move=False, align='left', font=FONT)
