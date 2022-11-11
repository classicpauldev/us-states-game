from turtle import Turtle
import pandas


# Create a StateEngine Class and inherit the Turtle Class
class StateEngine(Turtle):
    def __init__(self):
        super().__init__()
        self.reader = pandas.read_csv('50_states.csv')
        self.state_len = len(self.reader.state)
        self.current_guess = 0
        self.guessed_states = []
        self.do_not_rewrite = []
        self.missed_state = []
        self.hideturtle()
        self.penup()

# Create a function that checks the user input if valid or not
    def valid(self, state):
        for states in self.reader.state:
            if state == states:
                if state not in self.guessed_states:
                    self.guessed_states.append(state)
                    self.current_guess += 1
                return True
        print('Not a valid state')

# Create a function that go to the input state x-axis and y-axis and write the state inputted by the user
    def state_check(self, state):
        if state not in self.do_not_rewrite:
            get_row = self.reader[self.reader.state == state]
            x_axis = get_row['x']
            y_axis = get_row['y']
            self.goto(int(x_axis), int(y_axis))
            self.write(state)
        self.do_not_rewrite.append(state)

# Create a function that checks for missed states and write them to a csv file.
    def missed_states(self):
        for state in self.reader.state:
            if state not in self.guessed_states:
                self.missed_state.append(state)
        missed_states = {
            "states": self.missed_state
        }
        data_frame_missed_states = pandas.DataFrame(missed_states)
        self.missed_state = data_frame_missed_states.to_csv('states_to_learn.csv')
