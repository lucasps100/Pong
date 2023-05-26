from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.up()
        self.xmove = 15
        self.ymove = 15

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def bounce(self):
        self.ymove *= -1

    def hit(self):
        self.xmove *= -1
