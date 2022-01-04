from turtle import Turtle, Screen
import turtle
import random


is_race_on = False
screen = Screen()
screen.setup(width=700, height=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []


for turle_index in range(0, 6):
    new_turle = Turtle(shape="turtle")
    new_turle.color(colors[turle_index])
    new_turle.penup()
    new_turle.goto(x=-330, y=y_positions[turle_index])
    all_turtles.append(new_turle)


if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 315:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turle is the winner!")


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()