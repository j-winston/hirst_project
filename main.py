from colorgram import colorgram
from turtle import Turtle, Screen
import random

# initialize our turtle related objects
tim = Turtle()
tim.shape('turtle')
# set penup so turtle doesn't draw lines between dots
tim.penup()
# for updating our turtle's position
y_position = 0
x_position = 0

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

# draw 10x10 matrix of random colored dots
for each_row in range(10):
    for each_dot in range(10):
        tim.dot(20, random.choice(extracted_colors))
        tim.forward(50)
    y_position += 50
    x_position = 0
    # move turtle to the beginning of next row
    tim.sety(y_position)
    tim.setx(x_position)


screen.exitonclick()

