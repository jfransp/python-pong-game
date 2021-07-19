import turtle

wn = turtle.Screen() #Creates a screen object.
wn.title("Pong by @TokyoEdTech") #Attributes a title.
wn.bgcolor("black") #Establishes a background color.
wn.setup(width=800, height=500)
wn.tracer(0) #stops the window from updating(?)

# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) #speed of animation, sets the speed to the maximum speed.
paddle_a.shape("square") #20px20p por standard.
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) #Estica o formato x5 (como o padrão é 20, o resultado é 100p)
paddle_a.penup() #?
paddle_a.goto(-350, 0)


# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) #speed of animation, sets the speed to the maximum speed.
paddle_b.shape("square") #20px20p por standard.
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) #Estica o formato x5 (como o padrão é 20, o resultado é 100p)
paddle_b.penup() #?
paddle_b.goto(+350, 0)


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 215)
pen.write(f"Player A: {score_a} PlayerB: {score_b}",
          align="center", font=("Courier", 24, "normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor() #retorna a coordenada y
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() #retorna a coordenada y
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update() #Everytime the loop runs, it updates the screen.

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 240:
        ball.sety(240)
        ball.dy *= -1

    if ball.ycor() < -240:
        ball.sety(-240)
        ball.dy *= -1

    if ball.xcor() > 380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a} PlayerB: {score_b}",
                  align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a} PlayerB: {score_b}",
                  align="center", font=("Courier", 24, "normal"))

    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() -60:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() < 340 and ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() -60:
        ball.setx(-340)
        ball.dx *= -1
