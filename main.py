from colorgram import colorgram
from turtle import Turtle, Screen
import random

# initialize our turtle related objects
tim = Turtle()
tim.shape('turtle')
tim.speed('slow')
# set penup so turtle doesn't draw lines between dots
tim.penup()
# for updating our turtle's position
y_position = 0
x_position = 0
# set number of dots and rows
NUM_DOTS = 10
NUM_ROWS = 10

# initialize our screen objects
screen = Screen()
# set to rgb mode for random color later
screen.colormode(255)


# returns a list of tuple objects extracted from an image
def extract_color(file, num_colors):
    colors = colorgram.extract('fruit_salad.png', num_colors)
    color_list = []
    # the first extracted color is usually the background color, so skip it
    for color in colors[1:]:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        color_list.append(new_color)
    return color_list


# create list of tuples with rgb values from our image
extracted_colors = extract_color('fruit_salad.png', 30)


# MAIN LOOP ###

# put our turtle somewhere in the middle to start
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
x_position = tim.xcor()
y_position = tim.ycor()

# draw 10x10 matrix of random colored dots
for each_row in range(NUM_ROWS):
    for dots in range(NUM_DOTS):
        tim.dot(20, random.choice(extracted_colors))
        tim.forward(50)
        # at the end of each row move turtle up and back to the left
        if dots == 9:
            tim.setheading(90)
            tim.forward(50)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)
    y_position += 50
    # move turtle to the beginning of next row
    tim.sety(y_position)
    tim.setx(x_position)


screen.exitonclick()

