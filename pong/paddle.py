from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.new_y = 0
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        self.new_y = self.ycor() + 20
        self.goto(self.xcor(), self.new_y)

    def go_down(self):
        self.new_y = self.ycor() - 20
        self.goto(self.xcor(), self.new_y)
