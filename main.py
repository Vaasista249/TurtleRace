import turtle
import random
screen = turtle.Screen()

screen.setup(height= 400, width=500)
user_bet = turtle.textinput(title = "Make your bet", prompt="Which turtle will win the race? Guess the colour:")
colours = ["red","orange","yellow","green","blue","purple"]
y_cor = -70
all_turtles = []

for ink in colours:
    sita = turtle.Turtle(shape= "turtle")
    sita.color(ink)
    sita.penup()
    x_cor= -230
    sita.goto(x = x_cor,y = y_cor)
    y_cor = y_cor + 30
    all_turtles.append(sita)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on= False
            winning_colour = turtle.pencolor()
            if winning_colour==user_bet:
                print(f"You have won! The {winning_colour} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_colour} turtle is the winner!")

        random_distance = random.randint(0,10)
        turtle.forward(random_distance)


screen.exitonclick()
