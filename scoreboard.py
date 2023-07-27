from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.t_score = 0
        self.color('white')
        self.penup()
        self.ht()
        self.goto(0,270)
        self.write(f" Your Score is: {self.t_score}", move=False, align='center',font=("Arial", 12, 'normal'))
    def scored(self):
        self.clear()
        self.t_score += 1
        self.write(f" Your Score is: {self.t_score}", move=False, align='center', font=("Arial", 12, 'normal'))


    def game_over(self):
        self.goto(0, 0)
        self.write(f" GAMEOVER", move=False, align='center', font=("Arial", 12, 'normal'))
