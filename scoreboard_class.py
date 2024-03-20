from turtle import Screen, Turtle

class Scoreboard:
    def __init__(self):
        pass

    @staticmethod
    def create_screen(size):
        screen = Screen()
        screen.setup(width=size[0], height=size[1])
        screen.bgcolor('black')
        screen.tracer(0)
        return screen

