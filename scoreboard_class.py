import time
from turtle import Screen, Turtle



score = 0


class Scoreboard:
    def __init__(self, scoreboard, score):
        self.scoreboard = scoreboard
        self.score = score


    @staticmethod
    def create_screen(size):
        screen = Screen()
        screen.setup(width=size[0], height=size[1])
        screen.bgcolor('black')
        screen.tracer(0)
        return screen

    # @staticmethod
    def create_scoreboard(self):
        test = self.scoreboard

        scoreboard = Turtle()
        scoreboard.penup()
        scoreboard.color('white')
        scoreboard.goto(0, 260)
        scoreboard.write(f'Score: {self.score}', True, align="center", font=('Arial', 20, 'normal'))
        scoreboard.hideturtle()
        test.append(scoreboard)
        # scoreboard.clear()

    def increase_score(self, score):
        self.scoreboard[0].clear()
        self.scoreboard[0].goto(0, 260)
        self.scoreboard[0].write(f'Score: {score}', True, align="center", font=('Arial', 20, 'normal'))
        # board.hideturtle()

    # @staticmethod
    def game_over(self):

        scoreboard = Turtle()
        scoreboard.penup()
        scoreboard.color('white')
        scoreboard.goto(-10, 0)
        scoreboard.write('Game Over', True, align="center", font=('Arial', 20, 'normal'))
        scoreboard.hideturtle()
        # self.scoreboard[0].exitonclick()

    # @staticmethod
    # def clear(test):
    #     test.hideturtle()


