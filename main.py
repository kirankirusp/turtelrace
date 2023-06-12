import random
from turtle import Turtle,Screen
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet :", prompt="which turtel will win the race:")
colors = ["red", "orange", "yellow", "green", "blue", "purple", "brown"]
y_position = [-150, -100, -50, 0, 50, 100, 150]
all_turtle = []
for turtle_index in range (0, 7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-245, y=y_position[turtle_index])
    all_turtle.append(new_turtle)
if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you have won...! the {winning_color}  Won the race")
            else:
                print(f"you lose...! the {winning_color} won the race")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)
screen.exitonclick()
