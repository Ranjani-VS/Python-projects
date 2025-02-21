from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from blocks import Block
import time
from scoreboard import Scoreboard
s=Screen()
s.bgcolor("black")
s.setup(800,600)
s.title("Breakout")
s.tracer(0)
pad=Paddle((0,-250))
b=Ball()
scb=Scoreboard()
block=Block()
s.listen()
s.onkeypress(pad.righ,"Right")
s.onkeypress(pad.lef,"Left")
block.nblock()
is_game_on=True
while is_game_on:
    s.update()
    time.sleep(b.move_speed)
    b.move()
    if b.xcor()>300 or b.xcor()<-300:
        b.bounce_x()
        b.move()
    if b.ycor()>300:
        b.bounce_y()
        b.move()
    if b.distance(pad)<50 and b.ycor()>-330:
        b.bounce_y()
        b.move_speed *= 0.9
        b.move()

    if b.ycor()<-350 and b.distance(pad)>50:
        b.goto(0,-240)
        b.move_speed=0.1
        b.bounce_y()
        scb.lpoint()
    for i in block.row:
        for j in i:
            if j.distance(b) < 20:
                j.hideturtle()

            if scb.life>3:
                scb.gover()
                is_game_on=False


s.exitonclick()
