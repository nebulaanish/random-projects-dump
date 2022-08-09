from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.xmove = 10
        self.ymove = 10
        self.penup()
        self.color("white")
        self.shape("circle")
        self.goto(0, 0)
        self.move_speed = .05

    def move(self):
        new_x = self.xcor()+self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def bouncey(self):
        self.ymove *= -1

    def bouncex(self):
        self.xmove *= -1
        self.move_speed *= .9
      #   self.ymove *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bouncex()
        self.move_speed = .05
