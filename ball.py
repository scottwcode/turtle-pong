from turtle import Turtle
MOVE_DISTANCE = 10
INITIAL_BALL_SPEED = 0.1


class Ball(Turtle):
    """ Class to simulate a ball """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("turtle")
        self.penup()
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.ball_speed = INITIAL_BALL_SPEED

    def move(self):
        """ Move the ball in the direction it is travelling"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """ Simulate a bounce by reversing direction & Increase ball speed """
        self.y_move *= -1
        self.ball_speed *= 0.9

    def bounce_x(self):
        """ Simulate a bounce by reversing direction & Increase ball speed """
        self.x_move *= -1
        self.ball_speed *= 0.9

    def reset_position(self):
        """ Move ball back to the center """
        self.goto(0, 0)
        self.ball_speed = INITIAL_BALL_SPEED
        self.bounce_x()
