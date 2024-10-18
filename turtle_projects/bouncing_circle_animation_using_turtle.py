import turtle

# Set up the screen
wn = turtle.Screen()
wn.title("Bouncing Circle")
wn.bgcolor("black")
wn.setup(width=400, height=400)

# Create the circle object
circle = turtle.Turtle()
circle.shape("circle")
circle.color("white")
circle.penup()

# Define initial parameters
circle_speed = 2  # Speed of the circle
direction = 1  # 1 for right, -1 for left
max_x = wn.window_width() // 2  # Max X boundary (half of screen width)

# Function to move the circle
def move_circle():
    global direction
    x = circle.xcor()
    
    # If the circle hits the right or left edge, reverse direction
    if x >= max_x - 10 or x <= -max_x + 10:
        direction *= -1

    # Move the circle
    circle.setx(x + direction * circle_speed)
    
    # Keep moving the circle
    wn.ontimer(move_circle, 10)

# Start the movement
move_circle()

# Main loop to keep the window open
wn.mainloop()
