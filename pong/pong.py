import turtle
import os

wn = turtle.Screen()
wn.title("Pong by SuperHamster")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0) #stop window from updating

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0) # set a maximum speed of animation
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1) 
paddle_a.penup()
paddle_a.goto(-350,0)
 
# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0) # set a maximum speed of animation
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1) 
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0) # set a maximum speed of animation
ball.shape("circle")
ball.color("white") 
ball.penup()
ball.goto(0,0)
ball.dx = 2 # everytime ball moves, it moves by 2px
ball.dy = 2

# Pen
pen = turtle.Turtle() # 'turtle' for the module name, 'Turtle' for class name
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen. write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Function
def paddle_a_up():
    y = paddle_a.ycor() # get the current y value
    y += 20 # add 20 to current y value
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


# Keyboard binging  
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main game loop
while True:
    wn.update() # everytimes loop runs, update the screen

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    dir_path = os.path.dirname(os.path.realpath(__file__))
    sound_path = os.path.join(dir_path, 'bounce.wav')

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        os.system('afplay "{}"&'.format(sound_path))
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        os.system('afplay "{}"&'.format(sound_path))
    
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen. write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
 
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen. write(f"Player A: {score_a}  Player B: {score_b}", align="center", font=("Courier", 24, "normal"))
    
    # Paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system('afplay "{}"&'.format(sound_path))  
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system('afplay "{}"&'.format(sound_path))
