
import turtle
import math
import sys
from PIL import Image

# Function to draw the Trigonometric circle, axes, and labels
def main(action, num):
    def draw_trigonometric_circle(t):
        # Draw the axes
        t.color('black')
        t.penup()
        t.goto(-200, 0)
        t.pendown()
        t.goto(200, 0)
        t.penup()
        t.goto(0, -200)
        t.pendown()
        t.goto(0, 200)

        # Draw the Trigonometric circle
        t.penup()
        t.goto(0, -100)
        t.pendown()
        t.circle(100)

        # Draw the angles and labels
        for angle in range(0, 360, 30):
            radian_angle = math.radians(angle)
            x = 100 * math.cos(radian_angle)
            y = 100 * math.sin(radian_angle)

            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.goto(x, y)

            t.penup()
            t.goto(x, y)
            t.pendown()
            t.write(f"{angle}°", align="center" , font=("Arial", 16, "bold"))

    # Function to calculate and draw a right-angled triangle
    def draw_triangle_and_calculate(t, angle, trig_function):
        # Clear previous drawings
        t.clear()
        # Draw the Trigonometric circle, axes, and labels
        draw_trigonometric_circle(t)
        t.pencolor("orange")
        t.pensize(4)
        # Draw the right-angled triangle
        t.penup()
        t.goto(0, 0)
        t.pendown()
        t.goto(100 * math.cos(math.radians(angle)), 100 * math.sin(math.radians(angle)))
        t.goto(100 * math.cos(math.radians(angle)), 0)

        # Calculate the trigonometric function value
        if trig_function == "sine":
            value = math.sin(math.radians(angle))
        elif trig_function == "cosine":
            value = math.cos(math.radians(angle))
        elif trig_function == "tangent":
            value = math.tan(math.radians(angle))
        elif trig_function == "cotangent":
            value = 1 / math.tan(math.radians(angle))

        # Print the result in the console
        x=f"{trig_function.capitalize()}({angle}°): {value:.2f}"
        o = open("./outputimages/outputdata.txt" , "w")
        o.write(x)
        o.close()

        # Display the angle and the calculated trigonometric function value
        t.penup()
        t.goto(50 * math.cos(math.radians(angle)), 50 * math.sin(math.radians(angle)))
        t.pendown()
        t.write(f"{trig_function.capitalize()}: {value:.2f}", align="center")

    # Create a turtle instance
    t = turtle.Turtle()
    s = turtle.Screen()
    s.tracer(0)
    t.speed(0)
    t.pensize(2)
    draw_triangle_and_calculate(t, num, action)
    con = turtle.getcanvas()
    con.postscript(file="./outputimages/drawing.eps")
    img = Image.open("./outputimages/drawing.eps")
    img = img.convert("RGBA")  # Convert to RGBA mode
    data = img.getdata()

    # Create a new list for image data
    new_data = []
    for item in data:
        if item[0] in range(200, 256) and not (item[0] == 255 and item[1] == 165 and item[2] == 0):
            new_data.append((255, 255, 255, 0))  # Transparent
        else:
            new_data.append(item)


    # Update image with new data
    img.putdata(new_data)

    # Save the image without background
    img.save("./outputimages/drawing_no_background.png", "PNG")

    sys.exit(0)


main(sys.argv[1], int(sys.argv[2]))
