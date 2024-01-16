from turtle import Turtle
class Score(Turtle):
    def __init__(self,):
        super().__init__()
        self.score=0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.p1=0
        self.p2=0
        self.board()

    def board(self): 
        self.clear()   
        self.goto(280,280)
        self.write(f"score {self.p1}",align="center",font=("Courier,80,normal"))
        self.goto(-280,280)
        self.write(f"score {self.p2}",align="center",font=("Courier,80,normal"))
        
    def score1(self):
        self.p1+=1  
        self.board()
    def score2(self):
        self.p2+=1  
        self.board()
        
        