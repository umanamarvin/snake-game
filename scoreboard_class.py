from turtle import Screen, Turtle

score = 0


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

    @staticmethod
    def create_scoreboard():
        scoreboard = Turtle()
        scoreboard.penup()
        scoreboard.color('white')
        scoreboard.goto(150, 150)
        scoreboard.write(f'Score: {score}', True, align="center", font=('Arial', 20, 'normal'))
        scoreboard.hideturtle()

    # def increase_score(self, board):
    #     board.clear()
    #     board.write(f'Score: {self.score + 1}', True, align="center", font=('Arial', 20, 'normal'))
    #     # board.hideturtle()


