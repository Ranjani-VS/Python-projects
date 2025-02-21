from turtle import Turtle
FONT = ("Courier", 24, "bold")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.life=0
        self.level=0
        self.update_score()
    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.life,align="center",font=("Courier",50,"normal"))
        self.goto(100, 200)
        self.write(self.level,align="center",font=("Courier",50,"normal"))
    def lpoint(self):
        self.life+=1
        self.update_score()
    def rpoint(self):
        self.level+=1
        self.update_score()
    def gover(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
