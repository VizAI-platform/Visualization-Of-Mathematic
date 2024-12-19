import turtle
from PIL import Image
import sys
# Set up the turtle screen
screen = turtle.Screen()
screen.setup(width=1200, height=400)
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
t.penup()

# رسم محور مختصات
def draw_coordinate_table():
    turtle.pensize(1)
    turtle.speed(0)
    turtle.penup()
    turtle.goto(-255, 0)
    turtle.pendown()
    turtle.forward(500)

# رسم خط افقی از -50 تا 50 با تقسیمات 5
for i in range(-50, 50, 5):
    t.goto(i * 5, 0)
    t.write(str(i), align="center")
    t.goto(i * 5, -5)
    t.pendown()
    t.goto(i * 5, 5)
    t.penup()

draw_coordinate_table()
s.tracer(0)
# رسم محور عمودی
t.goto(0, -5)
t.pendown()
t.goto(0, 5)
t.penup()

# دریافت ورودی از کاربر
num1 = int(sys.argv[1])
num2 = int(sys.argv[3])
action = sys.argv[2]

def main(action ,num1  , num2):
# رسم خط برای عدد اول
    if action == '+':
        # تعیین جهت حرکت بر اساس مقدار عدد دوم
        t.setheading(0 if num2 >= 0 else 180)

        # رسم خط اول (آبی)
        t.goto(0, 20)
        t.pendown()
        t.pensize(3)
        t.pencolor('blue')
        t.goto(num1 * 5 , 20)  # خط اول با یک طول ثابت برای تست
        t.penup()

        # رسم خط دوم (نارنجی)
        t.goto(num1 * 5, 25)
        t.pendown()
        t.pensize(3)
        t.pencolor('orange')
        t.goto((num1 * 5) + (num2 * 5) , 25)  # خط دوم با طول ثابت
        t.penup()

        # محاسبه و رسم جمع دو عدد
        result = num1 + num2
        t.goto(0, 30)
        t.pendown()
        t.pensize(3)
        t.pencolor('green')
        t.goto(result * 5 , 30)
        t.penup()
        # محاسبه و نمایش جمع دو عدد
        x = num1 + num2
        o = open("./outputimages/outputdata.txt" , "w")
        o.write(f"{num1} %2B {num2} = {x}")
        o.close()
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
    elif action == "*":
        product = num1 * num2
        segment_length = product / num2

        # Draw the lines for the product of the two numbers and divide it based on num2

        for i in range(int(num2)):
            # Draw a colored line segment representing a part of the product with different colors
            t.goto((num1 + i * segment_length * 5) - 5, 24)
            t.pendown()
            t.pensize(3)

            if i % 2 == 0:
                t.pencolor('orange')
            else:
                t.pencolor('red')

            t.goto((num1 + (i + 1) * segment_length * 5) - 5, 24)
            t.penup()
        o = open("./outputimages/outputdata.txt" , "w")
        o.write(f"{num1} * {num2} = {product}")
        o.close()
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
    elif action == '/':
        segment_length = num1 / num2
        for i in range(num2):
            # Draw a colored line segment representing a part of the division
            t.goto((i * segment_length * 5) - 5, 24)
            t.pendown()
            t.pensize(3)

            if i % 2 == 0:
                t.pencolor('blue')
            else:
                t.pencolor('orange')

            t.goto(((i + 1) * segment_length * 5) - 5, 24)
            
            # Draw a small black circle at the end of each segment
            t.penup()
            t.goto(((i + 1) * segment_length * 5) - 5, 24)
            t.pendown()
            t.dot(5, "black")  # Draw a small black dot

            t.penup()
            o = open("./outputimages/outputdata.txt" , "w")
            o.write(f"{num1}/{num2}={segment_length}")
            o.close()
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
    elif action == 'show':
        t.goto(num1 * 5, 19)
        t.pendown()
        t.setheading(-90)
        t.color('orange')
        #t.circle(3)
        x = f"your number is = {num1}"
        o = open("./outputimages/outputdata.txt" , "w")
        o.write(str(x))
        o.close()
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

main(action ,num1 , num2)
