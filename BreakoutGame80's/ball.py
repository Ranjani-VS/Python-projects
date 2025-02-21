from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(1,1)
        self.penup()
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1
        self.goto(0,-240)
    def move(self):
        nx=self.xcor()+self.xmove
        ny=self.ycor()+self.ymove
        self.goto(nx,ny)
    def bounce_y(self):
        self.ymove*=-1
    def bounce_x(self):
        self.xmove*=-1
