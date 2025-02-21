from turtle import Turtle
TUPLE=[(0,-250)]
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1, 5)
        self.goto(position)

    def righ(self):
        new_x = self.xcor() + 20
        self.goto(new_x,self.ycor() )
    def lef(self):
        new_x = self.xcor() - 20
        self.goto(new_x,self.ycor() )
