# from turtle import Turtle, Screen
# import random, constants


# def generate_position():
#     random_x = random.randrange(-constants.MAX_STEP_X, constants.MAX_STEP_X, 20)
#     random_y = random.randrange(-constants.MAX_STEP_Y, constants.MAX_STEP_Y, 20)
#
#     return random_x, random_y
#
#
# class Food:
#
#     def __init__(self, body, screen):
#         self.body = body
#         self.screen = screen
#         self.food = 0
#
#     # @staticmethod
#     def create(self):
#         self.food = Turtle('circle')
#         self.food.color('green')
#         self.food.penup()
#         self.food.hideturtle()
#         return self.food
#
#     def reappear(self):
#         # body_positions = []
#         # for position in self.body:
#         #     body_positions.append(position.pos())
#         new_position = generate_position()
#         print("Random food position:", new_position)
#         self.food.goto(new_position)
#         self.food.showturtle()
#         print("Food position after reappear:", self.food.pos())
#
#     def food_collision(self):
#
#         head = self.body[0]
#         if head.distance(self.food) < 10:
#             print('Food Collision')
#             self.reappear()
#             return True
#         else:
#             return False
#
