from turtle import Screen, Turtle
BALL_WIDTH = 20


class Paddle(Turtle):
    """ Class to simulate a player's "paddle" """

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        """ Simulate moving a paddle up """
        new_y = self.ycor() + BALL_WIDTH
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """ Simulate moving a paddle down """
        new_y = self.ycor() - BALL_WIDTH
        self.goto(self.xcor(), new_y)
