import turtle
import pandas as pd
screen=turtle.Screen()
# code for map
screen.title("U.S states game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data=pd.read_csv("50_states.csv")
all_states=data["state"].to_list()

guessed_states=[]

# code for user input
while len(guessed_states) < 50 :

    answer_state=screen.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="what state name to guess??").title()
    if answer_state=='Exit':
            
        
        missing_states=[state for state in all_states if state not in guessed_states]
        new_data=pd.DataFrame(missing_states)
                
        print(missing_states)

        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data["state"]==answer_state]
        t.goto(int(state_data["x"]),int(state_data["y"]))
        t.write(state_data["state"].item())

# working with CSV
ohio=data[data["state"]=="Ohio"]
print(ohio["x"])
   
turtle.mainloop()


