from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.color('white')

        self.high_score = 0

    def write_scoreboard(self, score):
        self.goto(0, 250)
        self.clear()
        self.retrieve_score()
        self.write(f'Score: {score}    High Score: {self.high_score}', True, align="center", font=('Arial', 16, 'normal'))

    def retrieve_score(self):
        with open("high_score.txt") as file:
            self.high_score = file.read()

    def increase_high_score(self, high_score):
        current_high_score = int(self.high_score)
        if high_score > current_high_score:

            with open("high_score.txt", mode="w") as file:
                file.write(str(high_score))
