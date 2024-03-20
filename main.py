import time, constants
from snake_class import Snake
from food_class import Food
from scoreboard_class import Scoreboard

speed = 0.1
screen = Scoreboard.create_screen(constants.SCREEN_SIZE)

snake_body = []
snake = Snake(snake_body, screen)
snake.create()
food = Food(snake_body, screen)
food.create()
food.reappear()


game = True

while game:

    snake.move()
    screen.update()
    snake.control()
    if food.food_collision():
        snake.increase()
        speed = snake.go_faster(speed)
    game = snake.wall_collision()
    # game = snake.tail_collision()

    # if wall_col or tail_col:
    #     game = False

    time.sleep(speed)



    # screen.exitonclick()



