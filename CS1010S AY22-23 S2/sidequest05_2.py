from hi_graph_connect_ends import *
from mission03 import reduce
import math

##########
# Task 1 #
##########
def connect_ends_of(*args):
    return reduce(args,connect_ends)
def koch(c):
    return put_in_standard_position(connect_ends_of(c,
                                                    rotate(+math.pi/3)(c),
                                                    rotate(-math.pi/3)(c),
                                                    c))
def kochize(level):
    return repeated(koch,level)(unit_line)

def show_connected_koch(level, num_points):
    draw_connected(num_points, kochize(level))

show_connected_koch(0,1000)
show_connected_koch(1,1000)
show_connected_koch(2,4000)
show_connected_koch(3,4000)
show_connected_koch(5,10000)

def snowflake():
    return connect_ends_of(*(rotate(2*math.pi/3*(0.5 - i))(kochize(5)) for i in range(3)))

draw_connected_scaled(100000,snowflake())
