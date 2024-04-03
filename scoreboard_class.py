from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color('white')

    def write_scoreboard(self, score, high_score):
        self.goto(0, 250)
        self.clear()
        self.write(f'Score: {score}    High Score: {high_score}', True, align="center", font=('Arial', 16, 'normal'))
