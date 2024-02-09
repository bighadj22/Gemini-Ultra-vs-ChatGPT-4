import turtle
import time
import random

# Constants
DELAY = 0.1  # Adjust for game speed
SQUARE_SIZE = 20
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Set up the screen
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Simple Snake Game")
screen.bgcolor("lightgreen")
screen.tracer(0)  # Turn off automatic screen updates

# Create the snake's head
head = turtle.Turtle()
head.speed(0)  # Set animation speed to the fastest
head.shape("square")
head.color("black")
head.penup()  # Don't draw lines when moving
head.goto(0, 0)
head.direction = "stop"  # Snake starts stationary

# Create food 
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)  # Place initial food

# Snake body (starts empty)
segments = []  

# Score display
score = 0
high_score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.shape("square")
score_pen.color("black")
score_pen.penup()
score_pen.hideturtle()
score_pen.goto(0, SCREEN_HEIGHT / 2 - 60)
score_pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 20, "normal"))


# Functions to change snake's direction
def go_up():
    if head.direction != "down":  # Prevent immediate backtracking
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


# Move the snake's body 
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + SQUARE_SIZE)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - SQUARE_SIZE)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - SQUARE_SIZE)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + SQUARE_SIZE)


# Bind keyboard controls
screen.listen()
screen.onkeypress(go_up, "Up")
screen.onkeypress(go_down, "Down")
screen.onkeypress(go_left, "Left")
screen.onkeypress(go_right, "Right")

# Main game loop
while True:
    screen.update()  # Update the screen visuals

    # Check for collision with borders
    if head.xcor() > SCREEN_WIDTH/2 - SQUARE_SIZE  or head.xcor() < -SCREEN_WIDTH/2 + SQUARE_SIZE or \
       head.ycor() > SCREEN_HEIGHT/2 - SQUARE_SIZE or head.ycor() < -SCREEN_HEIGHT / 2 + SQUARE_SIZE:
        time.sleep(1)  # Pause momentarily on game over
        head.goto(0, 0)
        head.direction = "stop"

        # Reset snake body
        for segment in segments:
            segment.goto(1000, 1000)  # Hide offscreen
        segments.clear()  

        # Reset score
        score = 0
        update_scoreboard()

    # Check for food collision
    if head.distance(food) < SQUARE_SIZE:
        # Move food to a new random position
        x = random.randint(-SCREEN_WIDTH/2 + SQUARE_SIZE, SCREEN_WIDTH/2 - SQUARE_SIZE) 
        y = random.randint(-SCREEN_HEIGHT/2 + SQUARE_SIZE, SCREEN_HEIGHT/2 - SQUARE_SIZE)
