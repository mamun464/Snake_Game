from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0

    def scoreAdd(self):
            self.score+=1

    def showScore(self):
        self.hideturtle()
        self.color("White")
        self.pu()
        self.goto(0,275)
        self.clear()
        self.write(arg=f"Score: {self.score}",align='center',font=('courier', 15, 'normal'))


    def gameOver(self):
        self.goto(0, 0)

        self.write(arg=f"GAME OVER!", align='center', font=('courier', 20, 'normal'))

