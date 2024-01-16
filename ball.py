from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.penup()
        self.color("white")
        self.x=10
        self.y=10 #this value will be replaced by new value which we got in bounce function

    def move(self): 
        x = self.xcor()+self.x
        y = self.ycor()+self.y
        self.goto(x,y)
    def bounce_y(self):
        self.y*=-1 
    def bounce_x(self):
        self.x*=-1    
    def center(self):
        self.goto(0,0) 
        self.bounce_x()
        
    
