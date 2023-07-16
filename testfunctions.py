import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the speed of the turtle
my_turtle.speed(5)

# Draw a square
i = 100
while i > 0:
    i -=10
    side_length = i

for _ in range(8):
    my_turtle.forward(side_length)
    my_turtle.left(45)

# Hide the turtle
my_turtle.hideturtle()

# Keep the window open
turtle.done()

