from turtle import Turtle,Screen
import random
s=Screen()
s.setup(600,500)
box=s.textinput("turtle race game","select the colour and which turtle is going to win")
color=["red","blue","green","purple","yellow","orange","violet"]
ypos=[-180,-150,-120,-90,-60,-30,0]
group=[]
race_on=False
if box:
   race_on=True
for i in range(7):
    turtle=Turtle()
    turtle.penup()
    turtle.shape("turtle")
    turtle.goto(-290,ypos[i])
    turtle.color(color[i])
    group.append(turtle)
while race_on:
 for j in group:
    if j.xcor()>280:
       race_on=False
       winner=j.pencolor()
       if box==winner:
          print(f"{winner} color is winner and you won")
       else:
          print(f"{winner} color is winner and you lost")   
    distance=random.randint(1,20)
    j.forward(distance)
s.exitonclick()