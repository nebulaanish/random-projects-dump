from ctypes import alignment
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Cantora One", 20, "normal")


class Score(Turtle):
    def __init__(self, count):
        super().__init__()
        self.hideturtle()
        self.penup()
      #   self.shape("none")
        self.goto(-10, 260)
        self.color("white")
        self.count = count
        msg = f"ScoreBoard: {self.count}"
        self.write(arg=msg, align=ALIGNMENT, font=FONT)
        self.speed("fastest")

    def whiteboard_clear(self):
        self.clear

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GameOver", align=ALIGNMENT, font=FONT)
