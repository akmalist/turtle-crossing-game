from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.shape("turtle")
        self.setheading(90)

    def move(self):
        self.penup()
        new_y = self.ycor() + MOVE_DISTANCE
        self.penup()
        self.goto(0, new_y)



