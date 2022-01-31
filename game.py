#from handtrack import user_value
import random as rd
from comp_play import a
# tool values for the game
# 1-rock
# 2-paper
# 3-scissors
user_points = 0
comp_points = 0
round = 0
while (round != 10):
    print(rd.randint(1, 3))
    print(f'{a}sess')  # but here only one time value is taken from comp_play.

    round = round+1
