from turtle import Screen, Turtle, clearscreen
import random
screen = Screen()

screen.setup(width=610, height=400)
screen.bgcolor("black")
screen.title("PONG Game")

FONT = "Agency FB"
ftype = "bold"


sq1 = Turtle()
sq2 = Turtle()
sq3 = Turtle()
sq4 = Turtle()
sq5 = Turtle()
sq6 = Turtle()
sq7 = Turtle()
sq0 = Turtle()


e = 40
for t in [sq0, sq1, sq2, sq3]:
    t.hideturtle()
    t.shape("circle")
    t.color("white")
    t.speed(0)
    t.penup()
    t.goto(280.0, e)
    e = e-20
    t.setheading(90)
    t.showturtle()

a = [sq0, sq1, sq2, sq3]


q = 40
for t in [sq4, sq5, sq6, sq7]:
    t.hideturtle()
    t.shape("circle")
    t.color("white")
    t.speed(0)
    t.penup()
    t.goto(-290.0, q)
    q = q-20
    t.setheading(90)
    t.showturtle()
b = [sq4, sq5, sq6, sq7]



scor = Turtle()
scor.penup()
scor.hideturtle()
scor.color("white")
scor.goto(-40, 140)
scor2 = Turtle()
scor2.penup()
scor2.hideturtle()
scor2.color("white")
scor2.goto(20, 140)

class Hope:


    def __init__(self):
        self.a_ycor = []
        self.p1 = 0
        self.p2 = 0
        self.scor = scor
        self.scor2 = scor2
        self.board()
        screen.tracer(0,3)

    def board(self):

        if self.p1 == 0:
            self.scor.write(f"{str(self.p1)}", move=False, font=(FONT, 38, ftype))
        elif self.p1 > 0:
            self.scor.clear()
            self.scor.write(f"{str(self.p1)}", move=False, font=(FONT, 38, ftype))
        if self.p2 == 0:
            self.scor2.write(f"{str(self.p2)}", move=False, font=(FONT, 38, ftype))
        elif self.p2 > 0:
            self.scor2.clear()
            self.scor2.write(f"{str(self.p2)}", move=False, font=(FONT, 38, ftype))

    def s1_up(self):

        self.a_ycor = []
        if 190 >= a[0].ycor():
            for seg_num in a:
                seg_num.forward(30)
                self.a_ycor.append(seg_num.ycor())

    def s1_down(self):

        self.a_ycor = []
        if a[3].ycor() > -195:
            for seg_num in a:
                seg_num.backward(30)
                self.a_ycor.append(seg_num.ycor())

    def s2_up(self):

        self.b_ycor = []
        if 180 >= b[0].ycor():
            for seg_num in b:
                seg_num.forward(30)
                self.b_ycor.append(seg_num.ycor())

    def s2_down(self):

        self.b_ycor = []
        if b[3].ycor() > -185:
            for seg_num in b:
                seg_num.backward(30)
                self.b_ycor.append(seg_num.ycor())




class Sticks(Hope):
    screen.onkeypress(Hope().s1_up, "Up")
    screen.listen()
    screen.onkeypress(Hope().s1_down, "Down")
    screen.listen()
    screen.onkeypress(Hope().s2_up, "w")
    screen.listen()
    screen.onkeypress(Hope().s2_down, "s")
    screen.listen()


    def __init__(self):

        self.ball_screen = 25
        self.ball_speed = 2
        self.game_on = True
        super().__init__()
        self.lines()
        self.Wall_Up = []
        self.Wall_Down = []
        self.create_wall_up()
        self.create_wall_down()
        self.board()
        self.s1_up()
        self.s2_up()
        self.ball = Turtle()
        self.Ball()


    def Ball(self):
        self.board()
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.shapesize(0.5, 0.5)
        #self.ball.speed("slowest",0)
        self.ball.goto(0, 11)
        # self.ball.goto(-310, 0)
        screen.tracer(self.ball_speed, self.ball_screen)
        if self.p1 == self.p2:
            self.ball.setheading(random.choice([0, 180]))
        elif self.p1 > self.p2:
            self.ball.setheading(180)
        elif self.p1 < self.p2:
            self.ball.setheading(0)

        while self.game_on:
            self.ball.forward(1)

            if self.ball.xcor() > 315:
                self.p1 += 1

                self.game_on = False

            elif self.ball.xcor() < -315:
                self.p2 += 1

                self.game_on = False

            if self.ball.distance(sq3) < 30 or self.ball.distance(sq0) < 30:
                while True:

                    self.ball.forward(1)

                    for y in a:
                        if self.ball.distance(y) < 15:
                            if y == sq0:
                                self.ball.setheading(random.choice([120, 140, 150]))
                                break
                            elif y == sq2:
                                self.ball.setheading(random.choice([130, 170, 160]))
                                break
                            elif y == sq1:
                                self.ball.setheading(random.choice([200, 210, 230]))
                                break
                            elif y == sq3:
                                self.ball.setheading(random.choice([190, 220, 230]))
                                break
                    if self.ball.xcor() < -270:
                        break

                    if 200 > self.ball.ycor() > 187:
                        self.ball.setheading(random.choice([210, 230, 240]))
                    if -197 < self.ball.ycor() < -185:
                        self.ball.setheading(random.choice([120, 140, 130]))
                    if self.ball.xcor() > 330 or self.ball.xcor() < -330:
                        break

            if self.ball.distance(sq4) < 30 or self.ball.distance(sq7) < 30:
                while True:
                    # print(self.ball.pos())
                    xcor = self.ball.xcor()
                    self.ball.forward(1)
                    for y in b:
                        if self.ball.distance(y) < 15:
                            if y == sq5:
                                self.ball.setheading(random.choice([30, 45, 50]))
                                break
                            elif y == sq4:
                                self.ball.setheading(random.choice([320, 330, 340, 350]))
                                break
                            elif y == sq6:

                                self.ball.setheading(random.choice([315, 300, 305]))
                                break
                            elif y == sq7:
                                self.ball.setheading(random.choice([80, 75, 70]))
                                break
                    if self.ball.xcor() > 270:
                        break
                    if 200 > self.ball.ycor() > 187:
                        self.ball.setheading(random.choice([330, 320, 340]))
                        if self.ball.xcor() < xcor:
                            self.ball.setheading(0)

                    if -197 < self.ball.ycor() < -185:
                        self.ball.setheading(random.choice([50, 60, 45]))

                        # print(self.ball.pos())

                        if self.ball.xcor() < xcor:
                            self.ball.setheading(0)

                    if self.ball.xcor() > 330 or self.ball.xcor() < -330:
                        break


        self.game_on = True
        self.Ball()

    def lines(self):
        l = Turtle()
        l.color("white")
        l.shape("blank")
        l.pensize(2)
        l.penup()
        l.goto(0.0, -220)
        l.pencolor("white")
        l.left(90)
        for r in range(0, 20):
            l.forward(16)
            l.pendown()
            l.forward(5)
            l.penup()


    def create_wall_up(self):
        y = -290.0
        for s in range(0, 30):
            screen.tracer(0, 2)
            s = Turtle()
            s.hideturtle()
            s.color("white")
            s.shape("square")
            s.penup()
            s.goto(y, 205)
            y += 20
            s.showturtle()

            self.Wall_Up.append(s)

    def create_wall_down(self):
        y = -290.0
        for s in range(0, 30):
            screen.tracer(0, 2)
            s = Turtle()
            s.hideturtle()
            s.color("white")
            s.shape("square")
            s.penup()
            s.goto(y, -197)
            y += 20
            s.showturtle()

            self.Wall_Down.append(s)

Sticks()


screen.exitonclick()
