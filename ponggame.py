from turtle import Screen
from paddle import Paddle
from ball import Ball
from scorebord2 import Score
import time
s=Screen()
s.setup(800,600)
s.bgcolor("black")
s.title("pong game")
s.listen()
s.tracer(0)
p1=Paddle((350,0))
p2=Paddle((-350,0))
b=Ball()
s1=Score()
s.onkey(p1.up,"Up")
s.onkey(p1.down,"Down")
s.onkey(p2.up,"w")
s.onkey(p2.down,"s")

game_on=True
while game_on:
    time.sleep(0.1)
    s.update()
    b.move()
    if b.ycor()>280 or b.ycor()<-280:
        b.bounce_y()
    if b.distance(p1)<50 and b.xcor()>320 or b.distance(p2)<50 and b.xcor()<-320:
        b.bounce_x()
    if b.xcor()>390:
        b.center()
        s1.score2()
    if b.xcor()<-390:
        b.center()
        s1.score1()

s.exitonclick()