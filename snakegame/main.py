from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Xenzia")
screen.tracer(0)

snake = Snake()
food = Food()
count = 0
score = Score(count)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
game_on = True
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()

    # Score Tracker
    score.clear()
    score = Score(count)
    # Detect food collision
    if snake.head.distance(food) < 15:
        food.refresh()
        count += 1
        snake.extend()
   # Detect head collision
    x = snake.head.xcor()
    y = snake.head.ycor()
    if x > 290 or (x < -290) or (y > 290 or y < -290):
        game_on = False
    # detect self collision

    for segment in snake.segments:
        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False

if not game_on:
    score.game_over()


screen.exitonclick()
