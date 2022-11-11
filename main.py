from engine import StateEngine
import turtle

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.bgpic('blank_states_img.gif')
engine = StateEngine()
q = "What's another state name?"

while engine.current_guess != engine.state_len:
    # Capture the user input
    input_state = turtle.textinput(title=f"{engine.current_guess}/{engine.state_len} States Correct", prompt=q).title()
    # Stop the while loop if the user input "Exit"
    if input_state == "Exit":
        engine.missed_states()
        break
    # Check if the user input is valid
    if engine.valid(input_state):
        # Check if the input hasn't been made before and add it to the current guess count
        engine.state_check(input_state)
