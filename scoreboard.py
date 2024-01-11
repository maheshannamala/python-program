from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0,280)
        self.write(f"score {self.score}",align="center",font=("Arial,30,normal"))
        self.hideturtle()
    def game_over(self):
        self.goto(0,0) 
        self.write(f"game over",align="center",font=("Arial,30,normal"))   
    def increase_score(self):
        self.score+=1
        self.clear()
        self.write(f"score {self.score}",align="center",font=("Arial,20,normal"))
        
