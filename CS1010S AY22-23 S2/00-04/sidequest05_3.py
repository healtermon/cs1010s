from hi_graph_connect_ends import *


def revert(curve):
    return lambda t: curve(1-t)

def yj_dragonize(num_points , curve):
    if num_points == 0: return curve
    c = yj_dragonize(num_points -1, curve)
    return put_in_standard_position(connect_ends(rotate(pi/2)(c), c))

def dragonize(num_points , curve):
    if num_points == 0: return curve
    c = dragonize(num_points -1, curve)
    return put_in_standard_position(connect_ends(revert(rotate(pi/2)(c)), c))


# draw_connected_scaled(4096, yj_dragonize(12, unit_line))
