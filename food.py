from turtle import Turtle, up
from typing import Match
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(37, 95, 133)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        randomx = random.randint(-280,280)
        randomy = random.randint(-280,280)

        self.goto(randomx, randomy)