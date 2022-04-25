from colorgram import colorgram
from turtle import Turtle, Screen


# returns a list of tuple objects extracted from an image
def extract_color(file, num_colors):
    colors = colorgram.extract('fruit_salad.png', num_colors)
    color_list = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        color_list.append(new_color)
    return color_list

# create a list of 30 rgb color tuples
extracted_colors = extract_color('fruit_salad.png', 30)

print(extracted_colors)


