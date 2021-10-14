from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=600, height=600)
screen.colormode(255)
screen.bgcolor(200,224,135)
screen.tracer(0)

screen.title("Apple Hunt")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

gameState = True

while gameState:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Collision Detector
    if snake.head.distance(food) < 18:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()


    #Detect wall collision
    if snake.head.xcor() > 290 or  snake.head.xcor() < -290  or snake.head.ycor() > 290  or snake.head.ycor() < -290:
        scoreboard.game_over()
        gameState = False

    #Detect tail collision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            gameState = False

screen.exitonclick()