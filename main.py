import time
from turtle import Screen

from snake_class import Snake
from food_class import Food
from scoreboard_class import Scoreboard

timer = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.tracer(0)

snake = Snake()
snake.create_snake()

food = Food()
food.reappear()

score = 0
high_score = 0
scoreboard = Scoreboard()

game_on = True


def end_game():
    global game_on
    game_on = False


while game_on:

    scoreboard.write_scoreboard(score, high_score)

    snake.move()
    snake.control()

    if food.distance(snake.head) < 10:
        food.reappear()
        snake.increase()
        score += 1
        timer *= 0.9

    if snake.wall_collision() or snake.tail_collision():
        snake.reset_snake()
        timer = 0.1
        # snake.create_snake()
        food.reappear()
        if score > high_score:
            high_score = score
        score = 0

    time.sleep(timer)
    screen.update()

    screen.listen()
    screen.onkey(key="o", fun=end_game)
