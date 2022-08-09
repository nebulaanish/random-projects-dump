
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
      #   self.shape("none")
        self.color("white")

        self.count_left = 0
        self.count_right = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.count_left, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.count_right, align=ALIGNMENT,
                   font=FONT)
        self.speed()

    def leftup(self):
        self.count_left += 1
        self.update_score()

    def rightup(self):
        self.count_right += 1
        self.update_score()

    def whiteboard_clear(self):
        self.clear()

    def game_over(self):
        self.goto(0, 0)
        self.color("yellow")
        self.write(f"GameOver", align=ALIGNMENT,
                   font=("courier", 50, "normal"))
