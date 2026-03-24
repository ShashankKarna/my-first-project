# import turtle
# import random

# #setup screen
# screen =turtle.Screen()
# screen.bgcolor("black")
# screen.title("Roaming colorful Turtle")

# #create turtle
# t=turtle.Turtle()
# t.shape("turtle")
# t.speed(0) #fastest speed
# t.width(3)

# #list of colors
# colors=["red"+"blue"+"green"+"yellow"+"orange"]

# #Make turtle roam
# t.color(random.choice(colors)) #change color randomly
# t.forward(random.randint(20,60)) #Move forward random distance
# t.right(random.randint(0,360)) #Turn random direction

# import turtle

# screen = turtle.Screen()
# screen.bgcolor("black")

# t = turtle.Turtle()
# t.speed(0)
# t.width(2)

# colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# for i in range(200):
#     t.color(colors[i % 6])
#     t.forward(i * 2)
#     t.right(59)

# turtle.done()

# import turtle

# screen = turtle.Screen()
# screen.bgcolor("skyblue")

# t = turtle.Turtle()
# t.speed(0)

# colors = ["red", "blue", "green", "yellow", "purple"]

# for i in range(36):
#     t.color(colors[i % 5])
#     t.circle(100)
#     t.right(10)

# turtle.done()

# import turtle
# import random

# screen = turtle.Screen()
# screen.bgcolor("black")

# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()

# colors = ["red", "yellow", "blue", "green", "purple", "white"]

# for _ in range(30):
#     t.penup()
#     t.goto(random.randint(-200, 200), random.randint(-200, 200))
#     t.pendown()
#     t.color(random.choice(colors))

#     for i in range(36):
#         t.forward(50)
#         t.backward(50)
#         t.right(10)

# turtle.done()

# import turtle

# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.setup(600, 600)

# snake = turtle.Turtle()
# snake.shape("square")
# snake.color("green")
# snake.penup()

# def move_up():
#     y = snake.ycor()
#     snake.sety(y + 20)

# def move_down():
#     y = snake.ycor()
#     snake.sety(y - 20)

# def move_left():
#     x = snake.xcor()
#     snake.setx(x - 20)

# def move_right():
#     x = snake.xcor()
#     snake.setx(x + 20)

# screen.listen()
# screen.onkeypress(move_up, "Up")
# screen.onkeypress(move_down, "Down")
# screen.onkeypress(move_left, "Left")
# screen.onkeypress(move_right, "Right")

# turtle.done()


# import turtle

# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.setup(600, 600)

# ball = turtle.Turtle()
# ball.shape("circle")
# ball.color("red")
# ball.penup()
# ball.speed(0)

# dx = 3
# dy = 3

# while True:
#     ball.setx(ball.xcor() + dx)
#     ball.sety(ball.ycor() + dy)

#     if ball.xcor() > 290 or ball.xcor() < -290:
#         dx *= -1

#     if ball.ycor() > 290 or ball.ycor() < -290:
#         dy *= -1

# import turtle

# Setup screen
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("Fractal Tree - Portfolio Project")

# t = turtle.Turtle()
# t.color("lime")
# t.left(90)
# t.speed(0)
# t.width(2)
# t.penup()
# t.goto(0, -250)
# t.pendown()

# def draw_tree(branch_length):
#     if branch_length > 5:
#         t.forward(branch_length)

#         t.right(20)
#         draw_tree(branch_length - 15)

#         t.left(40)
#         draw_tree(branch_length - 15)

#         t.right(20)
#         t.backward(branch_length)

# draw_tree(100)

# turtle.done()

# import turtle

# # Screen setup
# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("Animated Growing Fractal Tree")

# t = turtle.Turtle()
# t.left(90)
# t.speed(0)
# t.hideturtle()
# t.penup()
# t.goto(0, -250)
# t.pendown()

# Turn off automatic screen updates for smooth animation
# screen.tracer(0)

# def draw_tree(branch_length):
#     if branch_length > 5:
        
#         # Change color based on branch size
#         if branch_length < 20:
#             t.color("green")
#             t.width(2)
#         else:
#             t.color("brown")
#             t.width(branch_length / 10)

#         t.forward(branch_length)
#         screen.update()

#         t.right(25)
#         draw_tree(branch_length - 15)

#         t.left(50)
#         draw_tree(branch_length - 15)

#         t.right(25)
#         t.backward(branch_length)
#         screen.update()

# draw_tree(100)

# turtle.done()
# 

import turtle
import random
import time

# -------------------------
# Screen Setup
# -------------------------
screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgcolor("#0b1d26")
screen.title("Night Forest Scene - Portfolio Project")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.left(90)

# -------------------------
# Draw Moon
# -------------------------
moon = turtle.Turtle()
moon.hideturtle()
moon.penup()
moon.goto(300, 200)
moon.color("#f5f3ce")
moon.begin_fill()
moon.circle(60)
moon.end_fill()

# -------------------------
# Create Stars
# -------------------------
stars = []

for _ in range(80):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.goto(random.randint(-480, 480), random.randint(-50, 330))
    star.shape("circle")
    star.shapesize(0.1, 0.1)
    star.color("white")
    star.showturtle()
    stars.append(star)

# -------------------------
# Tree Drawing Function
# -------------------------
def draw_tree(branch_length):
    if branch_length > 8:

        if branch_length < 20:
            t.color("lightgreen")
            t.width(2)
        else:
            t.color("#5c3a21")
            t.width(branch_length / 12)

        t.forward(branch_length)

        angle = random.randint(15, 30)

        t.right(angle)
        draw_tree(branch_length - random.randint(10, 15))

        t.left(angle * 2)
        draw_tree(branch_length - random.randint(10, 15))

        t.right(angle)
        t.backward(branch_length)

# -------------------------
# Draw Multiple Trees
# -------------------------
# for _ in range(7):
#     t.penup()
#     x_position = random.randint(-450, 450)
#     t.goto(x_position, -300)
#     t.setheading(90)
#     t.pendown()

#     tree_size = random.randint(80, 130)
#     draw_tree(tree_size)

# # -------------------------
# # Twinkling Stars Animation
# # -------------------------
# while True:
#     for star in stars:
#         if random.random() > 0.5:
#             star.color("white")
#         else:
#             star.color("#555555")
#     screen.update()
#     time.sleep(0.3)

import turtle
import random
import time

# -------------------------
# Screen Setup
# -------------------------
screen = turtle.Screen()
screen.setup(1000, 700)
screen.bgcolor("#0b1d26")
screen.title("Cinematic Forest Scene - Portfolio Level")
screen.tracer(0)

# -------------------------
# Sky Color Transition
# -------------------------
def sky_transition():
    colors = [
        "#0b1d26", "#102a3c", "#1b3b5a",
        "#355c7d", "#6c5b7b", "#f8b195"
    ]
    for color in colors:
        screen.bgcolor(color)
        screen.update()
        time.sleep(0.7)

# -------------------------
# Moon
# -------------------------
moon = turtle.Turtle()
moon.hideturtle()
moon.penup()
moon.goto(300, 200)
moon.color("#f5f3ce")
moon.begin_fill()
moon.circle(60)
moon.end_fill()

# -------------------------
# Stars
# -------------------------
stars = []
for _ in range(60):
    star = turtle.Turtle()
    star.hideturtle()
    star.penup()
    star.goto(random.randint(-480, 480), random.randint(-50, 330))
    star.shape("circle")
    star.shapesize(0.15, 0.15)
    star.color("white")
    star.showturtle()
    stars.append(star)

# -------------------------
# Shooting Star
# -------------------------
def shooting_star():
    star = turtle.Turtle()
    star.hideturtle()
    star.speed(0)
    star.penup()
    star.goto(-500, random.randint(100, 300))
    star.pendown()
    star.color("white")
    for _ in range(50):
        star.forward(15)
        star.right(2)
        screen.update()
    star.clear()

# -------------------------
# Tree Drawing
# -------------------------
tree = turtle.Turtle()
tree.hideturtle()
tree.speed(0)
tree.left(90)

def draw_tree(branch_length):
    if branch_length > 8:
        if branch_length < 20:
            tree.color("lightgreen")
            tree.width(2)
        else:
            tree.color("#5c3a21")
            tree.width(branch_length / 12)

        tree.forward(branch_length)

        angle = random.randint(15, 30)

        tree.right(angle)
        draw_tree(branch_length - random.randint(10, 15))

        tree.left(angle * 2)
        draw_tree(branch_length - random.randint(10, 15))

        tree.right(angle)
        tree.backward(branch_length)

# Draw multiple trees
for _ in range(6):
    tree.penup()
    tree.goto(random.randint(-450, 450), -300)
    tree.setheading(90)
    tree.pendown()
    draw_tree(random.randint(80, 120))

# -------------------------
# Falling Leaves
# -------------------------
leaves = []

for _ in range(20):
    leaf = turtle.Turtle()
    leaf.shape("circle")
    leaf.color("orange")
    leaf.shapesize(0.3, 0.3)
    leaf.penup()
    leaf.goto(random.randint(-400, 400), random.randint(0, 300))
    leaves.append(leaf)

# -------------------------
# Owl Silhouette
# -------------------------
owl = turtle.Turtle()
owl.hideturtle()
owl.penup()
owl.goto(0, -150)
owl.color("black")
owl.begin_fill()
owl.circle(20)  # Body
owl.end_fill()

# -------------------------
# Animation Loop
# -------------------------
counter = 0
while True:

    # Twinkling stars
    for star in stars:
        star.color("white" if random.random() > 0.5 else "#555555")

    # Falling leaves movement
    for leaf in leaves:
        leaf.sety(leaf.ycor() - random.randint(2, 5))
        leaf.setx(leaf.xcor() + random.randint(-2, 2))

        if leaf.ycor() < -320:
            leaf.goto(random.randint(-400, 400), 300)

    # Shooting star occasionally
    if random.random() > 0.995:
        shooting_star()

    # Sunrise transition after some time
    counter += 1
    if counter == 400:
        sky_transition()

    screen.update()
    time.sleep(0.03)