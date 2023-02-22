from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.highScore = 0
        with open("data.txt","r") as Store_score:
            self.highScore=int(Store_score.read())


        self.score=0
        self.hideturtle()
        self.color("White")
        self.pu()
        self.goto(0,275)
        self.showScore()

    def scoreAdd(self):
            self.score+=1

    def showScore(self):

        self.clear()
        self.write(arg=f"Score: {self.score} High Score:{self.highScore}",align='center',font=('courier', 15, 'normal'))

    def reset_scoreboard(self):
        if self.score>self.highScore:
            self.highScore=self.score
            with open("data.txt","w") as scoreInsert:
                scoreInsert.write(str(self.highScore))

        self.score=0

    # def gameOver(self):
    #     self.goto(0, 0)
    #
    #     self.write(arg=f"GAME OVER!", align='center', font=('courier', 20, 'normal'))

