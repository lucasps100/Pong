from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.color("white")
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 30
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 30
            self.goto(self.xcor(), new_y)