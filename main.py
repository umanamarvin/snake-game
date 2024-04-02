import time
from turtle import Screen
from snake_class import Snake
# from food_class import Food
# from scoreboard_class import Scoreboard

timer = 0.5

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("Black")
screen.tracer(0)

snake = Snake()
snake.create_snake()


game_on = True

# snake.move()

while game_on:
    snake.move()
    snake.control()

    if snake.wall_collision() or snake.tail_collision():
        game_on = False

    # snake.increase()

    time.sleep(timer)

    timer *= 1


    screen.update()
screen.exitonclick()




# speed = 0.1
# screen = Scoreboard.create_screen(constants.SCREEN_SIZE)
#
# snake_body = []
# snake = Snake(snake_body, screen)
# snake.create()
#
# food = Food(snake_body, screen)
# food.create()
# food.reappear()
#
# score_test = []
# score = 0
# high_score = 0
# scoreboard = Scoreboard(score_test, score)
# scoreboard.create_scoreboard()
#
# print(score)
#
# game = True
#
# while game:
#
#     snake.move()
#     screen.update()
#     snake.control()
#     if food.food_collision():
#         snake.increase()
#         # speed = snake.go_faster(speed)
#         score += 1
#         high_score += 1
#         scoreboard.increase_score(score, high_score)
#         print(score)
#     if snake.tail_collision() or snake.wall_collision():
#         scoreboard.game_over()
#         game = False
#
#     time.sleep(speed)
#
# screen.exitonclick()