import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import Scoreboard

snake = Snake()
screen = Screen()
score = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

food = Food()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
snake.create_snake()
while game_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.scored()

    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_on = False
        score.game_over()

    for segment in snake.segments:
        if segment == snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment) < 10:
            game_on = False
            score.game_over()


screen.exitonclick()