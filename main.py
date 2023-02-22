# Turtle Pong
# This is a rendition of the original Pong game played with a turtle as a ball.
# There are 2 players. Each player has a paddle they can move up and down to
# try to stop the "ball" from going past their paddle
#    l_paddle - along the left hand side of screen ('w' for up, 's' for down)
#    r_paddle - along the right hand side of screen (up arrow for up, down arrow for down)
# A point is scored if the "ball" goes past the other player's paddle
# The "ball" goes faster each time it hits a paddle
# Play continues indefinitely
#

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_WIDTH = 20
PADDLE_EDGE = 50
TOP_WALL_Y = int(SCREEN_HEIGHT/2-BALL_WIDTH)
BOTTOM_WALL_Y = int(-(SCREEN_HEIGHT/2-BALL_WIDTH))

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Turtle Pong")
screen.tracer(0)

r_paddle_x = int(SCREEN_WIDTH/2 - PADDLE_EDGE)  # 350
l_paddle_x = int(-(SCREEN_WIDTH/2 - PADDLE_EDGE))  # -350
r_paddle = Paddle((r_paddle_x, 0))
l_paddle = Paddle((l_paddle_x, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True
while game_on:
    # Set the speed of the ball
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collision with top/bottom wall
    if ball.ycor() > TOP_WALL_Y or ball.ycor() < BOTTOM_WALL_Y:
        ball.bounce_y()

    # Detect collision with a paddle
    if ball.distance(r_paddle) < PADDLE_EDGE and ball.xcor() > 320 or ball.distance(l_paddle) < PADDLE_EDGE and ball.xcor() < -320:
        ball.bounce_x()

    # Detect if r_paddle misses; ball goes past r_paddle
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect if l_paddle misses; ball goes past l_paddle
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
