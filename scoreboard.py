from turtle import Turtle


class Scoreboard(Turtle):
    """ class to simulate a scoreboard and keep track of each player's score """

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """ Update the scoreboard with the latest scores"""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center",
                   font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center",
                   font=("Courier", 80, "normal"))

    def l_point(self):
        " Give the player controlling the left paddle a point"
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        " Give the player controlling the right paddle a point"
        self.r_score += 1
        self.update_scoreboard()
