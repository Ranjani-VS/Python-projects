from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue"]
y=250
class Block:
    def __init__(self):
        self.li = []
        self.row=[]
    def nblock(self):
        global y
        for rc in range(0,1):
            # if rc==1:
            for colr in COLORS:
                for x in range(-280,280,45):
                    nc=Turtle("square")
                    nc.shapesize(2,2)
                    nc.color(colr)
                    nc.penup()
                    nc.goto(x,y)
                    self.li.append(nc)
                y=y-45
            self.row.append(self.li)
     

