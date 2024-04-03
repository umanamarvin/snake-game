from turtle import Turtle
import constants


class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.body = []
        self.head = None

    def create_snake(self):
        for location in constants.START_LOCATIONS:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            print(location)
            segment.goto(location)
            self.body.append(segment)

        print(self.body)
        self.head = self.body[0]

    def return_head(self):
        return self.head

    def move(self):
        new_location = self.head.pos()
        for segment in self.body:

            if segment == self.head:
                segment.forward(20)
            else:
                old_location = segment.pos()
                segment.goto(new_location)
                new_location = old_location

    def control(self):
        head = self.head

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
        head_pos = self.head.pos()
        if head_pos[0] <= -constants.HEAD_MAX_X or head_pos[0] >= constants.HEAD_MAX_X or head_pos[1] <= -constants.HEAD_MAX_Y or head_pos[1] >= constants.HEAD_MAX_Y:
            print('Wall Collision')
            return True
        else:
            return False

    def tail_collision(self):
        head = self.head
        rest_body = []

        for part in self.body:
            if part == head:
                pass
            else:
                rest_body.append(part)

        for part in rest_body:
            if head.distance(part) < 10:
                print('Tail collision')

                return True

    def increase(self):
        last_segment = self.body[-1]
        new_segment = last_segment.clone()
        self.body.append(new_segment)

    def reset_snake(self):
        for segment in self.body:
            segment.goto(1000,1000)
        self.body = []
        self.head = None
        print(self.body)
        self.create_snake()
