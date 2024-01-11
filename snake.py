from turtle import Turtle
CORDINATE=[(0,0),(-20,0),(-40,0)]
M=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:
    def __init__(self):
       self.segment=[]    
       self.createsnake()
       self.head=self.segment[0]
    def createsnake(self):
     for position in CORDINATE:
       self.add_segment(position)
      
    def add_segment(self,position):
      box=Turtle()
      box.shape("square")
      box.penup()
      box.color("white")
      box.goto(position)
      self.segment.append(box)

    def extend(self):
      self.add_segment(self.segment[-1].position())
    def move(self):
       for j in range(len(self.segment)-1,0,-1):
         x=self.segment[j-1].xcor()
         y=self.segment[j-1].ycor()
         self.segment[j].goto(x,y)
       self.head.forward(M)  
    def up(self):
      if self.head.heading() !=DOWN:
         self.head.setheading(UP)  
    def down(self):
      if self.head.heading() !=UP:
        self.head.setheading(DOWN) 
    def right(self):
      if self.head.heading() !=LEFT:
       self.head.setheading(RIGHT)
    def left(self): 
      if self.head.heading()!=RIGHT:
       self.head.setheading(LEFT)


       
    
 