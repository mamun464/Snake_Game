from turtle import Turtle,Screen
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20

class Snake:

    def __init__(self):
        self.allSnake = []
        self.crateSnake()
        self.head=self.allSnake[0]

    def crateSnake(self):
        for position in STARTING_POSITION:
            self.marge_sanke_segment(position)

    def marge_sanke_segment(self,position):
        snake = Turtle(shape="square")
        snake.color("white")
        snake.pu()
        snake.goto(position)
        self.allSnake.append(snake)


    def after_food(self):
        self.marge_sanke_segment(self.allSnake[-1].position())


    def move(self):
        for snake_index in range(len(self.allSnake) - 1, 0, -1):
            x = self.allSnake[snake_index - 1].xcor()
            y = self.allSnake[snake_index - 1].ycor()
            self.allSnake[snake_index].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for sanke in self.allSnake:
            sanke.goto(1000,1000)
        self.allSnake.clear()
        self.crateSnake()
        self.head=self.allSnake[0]

    def Up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def Down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def Left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def Right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

