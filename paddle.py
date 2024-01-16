from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,goto):
      super().__init__()
      self.shape("square")
      self.penup()
      self.color("white")
      self.shapesize(stretch_wid=5,stretch_len=1)
      self.goto(goto)
    def up(self):
     a=self.ycor()+20
     self.goto(self.xcor(),a)
    def down(self):
     a=self.ycor()-20
     self.goto(self.xcor(),a)  

