from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
racing = False
user_bet = screen.textinput(title="Place your bets!", prompt="Which turtle will win the race? Enter either "
                                                             "red/orange/yellow/green/blue/purple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []
y_cord = -100

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_cord)
    y_cord += 40
    turtles.append(new_turtle)

if user_bet:
    racing = True

while racing:
    for turtle in turtles:
        if turtle.xcor() > 230:
            racing = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
