import turtle
from turtle import Turtle, exitonclick, Screen
import random

# import colorgram
#
# colors = colorgram.extract('image.jpg', 20)
# my_colors = []
#
# for color in colors:
#     my_color = (color.rgb.r, color.rgb.g, color.rgb.b)
#     my_colors.append(my_color)
#
#
# print(my_colors)

tim = Turtle()
turtle.colormode(255)
tim.shape("turtle")
tim.color("purple")
tim.speed("fastest")
color_list = [(23, 16, 94), (232, 43, 6), (153, 14, 30), (41, 181, 158), (127, 253, 206), (237, 71, 166),
              (209, 179, 208), (246, 218, 21), (40, 133, 242), (244, 247, 253), (246, 218, 5), (207, 148, 178),
              (126, 155, 204), (106, 189, 174), (224, 134, 117), (81, 87, 136), (150, 64, 75)]


tim.penup()
y_position = -300
for _ in range(13):
    tim.setpos(-300, y_position)
    y_position += 50
    for _ in range(12):
        tim.color(23, 16, 94)
        tim.dot(20, (random.choice(color_list)))
        tim.forward(50)


screen = Screen()
screen.exitonclick()


