import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen=Screen()
screen.title("Snake Game")
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)
screen.listen()

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.onkey(fun= snake.Up, key= "Up")
screen.onkey(fun=snake.Down, key="Down")
screen.onkey(fun=snake.Left, key="Left")
screen.onkey(fun=snake.Right, key="Right")



star_game=True
while star_game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.showScore()

    #collision with food
    if snake.head.distance(food)<15:
        scoreboard.speed("fastest")
        scoreboard.scoreAdd()
        food.food_move()
        snake.after_food()

    # collision with Wall
    if snake.head.xcor()>=280 or snake.head.xcor() <= -280 or snake.head.ycor()>=280 or snake.head.ycor()<=-280:
        scoreboard.reset_scoreboard()
        snake.reset_snake()

    # collision with tail
    for segment in snake.allSnake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_snake()



screen.exitonclick()