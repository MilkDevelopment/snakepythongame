from turtle import Turtle, up
from typing import Match
import random

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__() 
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align="center", font=("Courrier",18))

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game over!", align="center", font=("Courrier",35))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        