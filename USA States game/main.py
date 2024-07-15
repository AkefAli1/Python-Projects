import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
name = Turtle()
name.hideturtle()
name.penup()

data = pandas.read_csv("50_states.csv")
state_list = list(data.state)
x_list = list(data.x)
y_list = list(data.y)

list_of_guesses = []


while len(list_of_guesses) < 50:
    number_of_correct = len(list_of_guesses)
    answer_state = str(screen.textinput(title=f"{number_of_correct}/50 states correct", prompt="Guess another state"))
    answer = answer_state.title()

    if answer == "Exit":
        break
    if answer in state_list:
        list_of_guesses.append(answer)
        a = data[data["state"] == answer]
        name.goto(x=int(a.x), y=int(a.y))
        name.write(answer, align="center", font=("Courier", 8, "normal"))
        #instead of writing answer you can also write a.state.item()
        #this method fetches the first item from the row

missed_states = []
for state in state_list:
    if state not in list_of_guesses:
        missed_states.append(state)
print(missed_states)
new_data = pandas.DataFrame(missed_states)
new_data.to_csv("missed_states.csv")



















