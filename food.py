import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.pu()
        self.color("red")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.food_move()
##food move when colission with sanke
    def food_move(self):
        random_x = random.randint(-265, 265)
        random_y = random.randint(-265, 265)
        self.goto(random_x, random_y)


        
