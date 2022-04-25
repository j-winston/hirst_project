from colorgram import colorgram


# return list of tuple objects extracted from an image
def extract_color(file, num_colors):
    colors = colorgram.extract('fruit_salad.png', num_colors)
    color_list = []
    for color in colors:
        rgb = color.rgb
        color_list.append(tuple(rgb))

    return color_list


extracted_colors = extract_color('fruit_salad.png', 8)

for rgb in extracted_colors:
    print(rgb)


