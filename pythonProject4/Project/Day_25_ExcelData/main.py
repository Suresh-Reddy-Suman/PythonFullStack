from turtle import Turtle as tim, Screen as sc
from location import Location
import pandas

from Score_board import ScoreBoard

GAME_OVER = False

my_screen = sc()
my_screen.setup(width=725, height=491)
my_screen.bgpic("blank_states_img.gif")
scoreboard = ScoreBoard()
my_screen.tracer(0)
updated_countries = []
missed_state = []

while not GAME_OVER:
    provided_state = my_screen.textinput(title='Remember the country', prompt="Provide the country name").title()
    data = pandas.read_csv("50_states.csv")

    countries = data["state"].tolist()
    if provided_state in countries:
        state_date = data[data['state'] == provided_state]
        place = Location(provided_state, state_date.x.item(), state_date.y.item())
        if provided_state not in updated_countries:
            updated_countries.append(provided_state)
            scoreboard.update_score()
    elif provided_state == 'Off':
        missed_state = [state for state in countries if state not in updated_countries]
        learning = {
            "State to Know": missed_state
        }
        pandas.DataFrame(learning).to_csv('State to Learn.csv')
        break
my_screen.update()
