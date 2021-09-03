import turtle
import winsound

t = turtle.Screen()
t.title("Pong Game")
t.bgcolor("black")
t.setup(width=800, height=600)
t.tracer(0)

#paddle_a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 0.9)
paddle_a.penup()
paddle_a.goto(-350, 0)

#paddle_b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 0.9)
paddle_b.penup()
paddle_b.goto(350, 0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1

#players
player = turtle.Turtle()
player.speed()
player.color("white")
player.penup()
player.hideturtle()
player.goto(0, 250)
Player_A, Player_B = map(str,input().split(" "))
player.write(f"{Player_A}:0  {Player_B}:0", align="center", font=("Courier", 24, "normal")) 
 

score_a = 0
score_b = 0

#functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard part
t.listen()
t.onkeypress(paddle_a_up, "w")
t.onkeypress(paddle_a_down, "s")
t.onkeypress(paddle_b_up, "p")
t.onkeypress(paddle_b_down, "l")

while True:
    t.update()

    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #checking border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -285:
        ball.sety(-285)
        ball.dy *= -1

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        player.clear()
        player.write(f"{Player_A}:{score_a}  {Player_B}:{score_b}", align="center", font=("Courier", 24, "normal")) 
        winsound.Beep(800, 150)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        player.clear()
        player.write(f"{Player_A}:{score_a}  {Player_B}:{score_b}", align="center", font=("Courier", 24, "normal")) 
        winsound.Beep(800,150)

    #paddle and ball collisions
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor() < paddle_b.ycor()+40 and ball.ycor() > paddle_b.ycor()-40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor()+40 and ball.ycor() > paddle_a.ycor()-40):
        ball.setx(-340)
        ball.dx *= -1

    #winner part
    if score_a == 10:
        ball.goto(0,0)
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        player.goto(0, 230)
        player.clear()
        player.write(f"{Player_A} wins!", align="center", font=("Courier", 35, "bold"))

    elif score_b == 10:
        ball.goto(0,0)
        paddle_a.goto(-350, 0)
        paddle_b.goto(350, 0)
        player.goto(0, 230)
        player.clear()
        player.write(f"{Player_B} wins!", align="center", font=("Courier", 35, "bold"))


