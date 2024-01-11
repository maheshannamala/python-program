from turtle import Screen
from scoreboard import Score
from food import Food
from snake import Snake
import time
s=Screen()
s.setup(600,600)
s.bgcolor("black")
s.title("snake game")
s.tracer(0)
s.listen()
snake=Snake()
food=Food()
score=Score()
s.onkey(snake.up,"Up")
s.onkey(snake.down,"Down")
s.onkey(snake.left,"Left")
s.onkey(snake.right,"Right")

game_on=True    
while game_on:
 s.update()
 time.sleep(0.1)
 snake.move()
 if snake.head.distance(food) <15:
  food.refresh()
  snake.extend()
  score.increase_score()
 if snake.head.xcor()>290 or snake.head.xcor()<-300 or snake.head.ycor()>300 or snake.head.ycor()<-290:
  game_on=False
  score.game_over()
 for seg in snake.segment[1:]:
  if snake.head.distance(seg)<10:
   game_on=False
   score.game_over()

s.exitonclick()    