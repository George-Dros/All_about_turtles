import turtle
from turtle import Turtle,Screen
from random import choice,randint

is_race_on =  False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make  your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

for number in range(0,6):
    new_turtle = Turtle("turtle")
    color = choice(colors)
    new_turtle.color(color)
    i = colors.index(color)
    colors.remove(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-235, y=-120 + number * 50)
    turtles.append(new_turtle)



if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print("You won!")
            else:
                print(f"You lost! The {winner} turtle won...")


        step = randint(0,10)
        turtle.forward(step)



screen.exitonclick()
