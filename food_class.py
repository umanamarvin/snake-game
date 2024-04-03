from turtle import Turtle
import random, constants


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('green')
        self.penup()

    def reappear(self):
        random_x = random.randrange(-constants.MAX_STEP_X, constants.MAX_STEP_X, 20)
        random_y = random.randrange(-constants.MAX_STEP_Y, constants.MAX_STEP_Y, 20)

        self.goto(random_x, random_y)
