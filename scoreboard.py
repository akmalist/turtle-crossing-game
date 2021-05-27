from turtle import Turtle

FONT = ("Courier", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font = FONT)

    def update_score(self):
        self.clear()
        self.goto(-220, 250)
        self.write(f"LEVEL: {self.level}", align="center", font =FONT)

    def increase_point(self):
        self.level +=1
        self.update_score()