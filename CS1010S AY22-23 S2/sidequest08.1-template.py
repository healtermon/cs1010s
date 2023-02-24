#
# CS1010S --- Programming Methodology
#
# Side Quest 8.1 Template
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.

from planets import *

##########
# Task 1 #
##########
# a)
# Follows trigonometry angle.
# E.g. 0 degree -> East
# E.g. 90 degree -> North
def get_velocity_component(angle, velocity):
    pass # remove and replace with your code

# print(get_velocity_component(30, 50)) # (43.30127018922194, 24.999999999999996)
# note that the exact values of each component may differ slightly due to differences in precision

# b)
def calculate_total_acceleration(planets, current_x, current_y):
    pass # remove and replace with your code

# print(calculate_total_acceleration(planets, 0.1, 0.1)) # (-1423.6113504393045, -1425.4297228686778)

# c)
# Do not change the return statement
def f(t, Y):
    # your code here
    return np.array([vx, vy, ax, ay])

np.set_printoptions(precision=5)
# print(f(0.5, [0.1, 0.1, 15.123, 20.211])) # [15.123  20.211  -1423.61135  -1425.42972]

##########
# Task 2 #
##########

# Uncomment and change the input parameters to alter the path of the spacecraft
# vx, vy = get_velocity_component(..., ...)


##############################################################################################
# Uncomment the following line to start the plot
# start_spacecraft_animation(vx, vy, f)
