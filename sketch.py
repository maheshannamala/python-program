from turtle import Turtle,Screen
tim=Turtle()
s=Screen()
def forward():
    tim.forward(10)
def backward():
    tim.backward(10) 
def left():
    a=tim.heading()+10
    tim.setheading(a)   
def right():
    a=tim.heading()-10
    tim.setheading(a)  
def erase():
    tim.clear()
    tim.penup()     
    tim.home()  
    tim.pendown()
s.listen()
s.onkey(forward,"d")
s.onkey(backward,"a")
s.onkey(left,"w")
s.onkey(right,"s")
s.onkey(erase,"c")
s.exitonclick()