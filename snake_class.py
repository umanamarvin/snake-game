import time
from turtle import Turtle, Screen
import constants


class Snake:
    def __init__(self, body, screen):
        self.body = body
        self.screen = screen

    def create(self):
        # initial_positions = [(0, 0), (-20, 0), (-40, 0), (-60, 0), (-80, 0), (-100, 0), (-120, 0), (-140, 0), (-160, 0)]
        initial_positions = [(0, 0), (-20, 0), (-40, 0)]
        for position in initial_positions:
            part = Turtle('square')
            part.penup()
            part.color('white')
            part.goto(position)
            self.body.append(part)
            # print(part)

    def move(self):
        new_position = self.body[0].pos()
        # print(new_position)
        self.body[0].forward(20)

        for part in self.body:
            if part == self.body[0]:
                pass
            else:
                old_position = part.pos()
                part.goto(new_position)
                new_position = old_position

    def extend(self):
        pass

    def control(self):

        head = self.body[0]

        def go_up():
            if head.heading() != 270:
                self.body[0].setheading(90)

        def go_down():
            if head.heading() != 90:
                self.body[0].setheading(270)

        def go_left():
            if head.heading() != 0:
                self.body[0].setheading(180)

        def go_right():
            if head.heading() != 180:
                self.body[0].setheading(0)

        self.screen.listen()
        self.screen.onkey(key=constants.UP, fun=go_up)
        self.screen.onkey(key=constants.DOWN, fun=go_down)
        self.screen.onkey(key=constants.LEFT, fun=go_left)
        self.screen.onkey(key=constants.RIGHT, fun=go_right)

    def wall_collision(self):

        head_pos = self.body[0].pos()
        if head_pos[0] <= -constants.HEAD_MAX_X or head_pos[0] >= constants.HEAD_MAX_X or head_pos[1] <= -constants.HEAD_MAX_Y or head_pos[1] >= constants.MAX_STEP_Y:
            print('Wall Collision')
            return False
        else:
            return True

    # def tail_collision(self):
    #     head_pos = self.body[0].pos()
    #     head_x = head_pos[0]
    #     head_y = head_pos[1]
    #     body = []
    #     for segment in self.body:
    #         if segment.pos() == head_pos or segment.pos() == self.body[1].pos():
    #             pass
    #         else:
    #             body.append(segment.pos())
    #
    #     for position in body:
    #
    #         position_x = position[0]
    #         position_y = position[1]
    #
    #         # Calculate the distance between the snake's head and the food
    #         distance = ((head_x - position_x) ** 2 + (head_y - position_y) ** 2) ** 0.5
    #
    #         if distance < 25:  # Adjust the threshold as needed
    #             print('Tail Collision')
    #             return False
    #         else:
    #             return True

    def increase(self):
        # print(self.body)
        last_segment = self.body[-1]
        new_segment = last_segment.clone()
        self.body.append(new_segment)

    @staticmethod
    def go_faster(time):
        new_time = time - (time*0.1)
        return new_time



