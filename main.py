from turtle import Turtle, Screen
from paddle import *
from ball import *
from scoreboard import *
import time


screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

writer = Turtle()
writer.speed("fastest")
writer.pencolor("white")
writer.hideturtle()
writer.penup()
writer.goto(0,-300)
writer.setheading(90)
for i in range(1, 30):
    writer.pendown()
    writer.forward(10)
    writer.up()
    writer.forward(10)

screen.listen()

paddle1 = Paddle((470,0))
paddle2 = Paddle((-470,0))
ball = Ball()
scoreboard = Scoreboard()


screen.onkeypress(paddle1.go_up, "Up")
screen.onkeypress(paddle2.go_up, "w")
screen.onkeypress(paddle1.go_down, "Down")
screen.onkeypress(paddle2.go_down, "s")

game_on = True
rally_count = 0

while game_on:
    screen.update()
    ball.move()
    time.sleep(.1)
    #detect collision with upper walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    # detect hit from paddle
    if ball.distance(paddle1) < 50 and ball.xcor() > 440 or ball.distance(paddle2) < 50 and ball.xcor() < -440:
        ball.hit()
        ball.xmove *= 1.1
        ball.ymove *= 1.1
        rally_count += 1

    # detect a miss
    if ball.xcor() > 500:
        ball.goto(0,0)
        ball.hit()
        scoreboard.p2_point()
        ball.xmove /= (1.1**rally_count)
        ball.ymove /= (1.1**rally_count)
        rally_count = 0

    if ball.xcor() < -500:
        ball.goto(0, 0)
        ball.hit()
        scoreboard.p1_point()
        ball.xmove /= (1.1 ** rally_count)
        ball.ymove /= (1.1 ** rally_count)
        rally_count = 0









screen.exitonclick()