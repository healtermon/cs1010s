from hi_graph import *
from mission04 import test_curve, reflect_through_y_axis

def connect_ends(curve1, curve2):
    return connect_rigidly(curve1,translate(x_of(curve1(1))-x_of(curve2(0)),
                                            y_of(curve1(1))-y_of(curve2(0)))(curve2))

# draw_connected_scaled(200, connect_rigidly(test_curve,reflect_through_y_axis(test_curve)))

def 

