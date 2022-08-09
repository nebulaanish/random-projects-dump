from sys import set_coroutine_origin_tracking_depth
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score
screen = Screen()

screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle_left = Paddle((-350, 0))
paddle_right = Paddle((350, 0))
ball = Ball()


screen.listen()
screen.onkey(paddle_left.go_up, "w")
screen.onkey(paddle_left.go_down, "s")

screen.onkey(paddle_right.go_up, "Up")
screen.onkey(paddle_right.go_down, "Down")

score = Score()

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #  collision  check with upper/lower walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()
    # detect collision with right paddle
    if ball.xcor() > 320 and ball.distance(paddle_right) < 50:
        ball.bouncex()
        # detect  collision with left paddle
    if ball.xcor() < -320 and ball.distance(paddle_left) < 50:
        ball.bouncex()
    # collision check with side walls
    if ball.xcor() > 380:
        score.leftup()
        ball.reset_position()
    if ball.xcor() < -380:
        score.rightup()
        ball.reset_position()
    if score.count_left >= 5 or score.count_right >= 5:
        game_on = False
if not game_on:
    score.game_over()
screen.exitonclick()
