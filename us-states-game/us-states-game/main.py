from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle()
turtle.shape(image)


message = "Guess the state"
correctly_guessed_states = []
data = pd.read_csv("50_states.csv")

while len(correctly_guessed_states) < 50:
    answer_state = (screen.textinput(title=message, prompt="What's another states name")).title()
    if answer_state == "Exit":
        missing_states = [item for item in data.state if item not in correctly_guessed_states]
        states_to_learn = pd.DataFrame(missing_states)
        states_to_learn.to_csv("states_to_learn.csv")
        break
    for state in data.state:
        if answer_state in correctly_guessed_states:
            pass
        elif state == answer_state:
            message = f"{len(correctly_guessed_states)+1}/50 States Correct"
            inputted_state = data[data.state == state]
            t = Turtle()
            t.penup()
            t.hideturtle()
            t.goto(float(inputted_state.x), float(inputted_state.y))
            t.write(answer_state)
            correctly_guessed_states.append(answer_state)
