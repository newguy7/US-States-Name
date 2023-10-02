import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# to get the coordinate when the mouse is clicked on the image
# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# to keep the screen open even after the code is finished running
# turtle.mainloop()


# Read the 50_states.csv file
data = pandas.read_csv("50_states.csv")
all_state_data = data.state.to_list()

guessed_state = []


while len(guessed_state)<50:
    # ask the user to guess the state name
    #answer_state = screen.textinput(title="Guess the state", prompt="What's another state name?").title()
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct", prompt="What's another state name? (Type Exit to see the result)").title()
    #print(answer_state)

    if answer_state == "Exit":
        break

    # check if the answer is correct
    if (answer_state in all_state_data):
        if (answer_state not in guessed_state):
            guessed_state.append(answer_state)

            # create of Turtle object
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()            

            state_data = data[data.state == answer_state]
            #t.goto(int(state_data.x), int(state_data.y))
            t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
            t.write(answer_state)
        # t.write(state_data.state.item())  
        
print(f"Congratulations you have answered {len(guessed_state)} states correctly")         

# Save the missed states in a list
missed_state = []

for state in all_state_data:
    if state not in guessed_state:
        missed_state.append(state)

print(missed_state)

# Save the missed state in a csv file
missed_state_dict = {
    "State" : missed_state
}
missed_state_data = pandas.DataFrame(missed_state_dict)
missed_state_data.to_csv("missing state.csv")
    


screen.exitonclick()