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

    @staticmethod
    def create_scoreboard(score):
        scoreboard = Turtle()
        scoreboard.penup()
        scoreboard.color('white')
        scoreboard.goto(150, 150)
        scoreboard.write(f'Score: {score}', True, align="center", font=('Arial', 20, 'normal'))
        scoreboard.hideturtle()

    @staticmethod
    def increase_score(board, score):
        board.write(f'Score: {score}', True, align="center", font=('Arial', 20, 'normal'))



