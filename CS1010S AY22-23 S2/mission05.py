from hi_graph import *
from math import sqrt
from mission04 import test_curve, reflect_through_y_axis

def connect_ends(curve1, curve2):
    return connect_rigidly(curve1,translate(x_of(curve1(1))-x_of(curve2(0)),
                                            y_of(curve1(1))-y_of(curve2(0)))(curve2))

# draw_connected_scaled(200, connect_rigidly(test_curve,reflect_through_y_axis(test_curve)))
# translate scale_xy rotate
gosperize
def my_gosperize(curve):
    scaled = scale(sqrt(2)/2)(curve)
    return connect_ends(rotate(+pi/4)(scaled),
                        rotate(-pi/4)(scaled))
def my_gosper_curve(level):
    return repeated(my_gosperize,level)

def my_gosper_curve_task2(level):
    return repeated(gosperize,level)
def show_points_gosper(level, num_points, initial_curve):
    draw_points(num_points,
                squeeze_curve_to_rect(-0.5, -0.5, 1.5, 1.5)\
                (my_gosper_curve_task2(level)(initial_curve)))

show_points_gosper(5,200,unit_line)
show_points_gosper(7,1000,arc)
show_points_gosper(5,500,arc)

gosper_curve_with_angle

def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0:
        return unit_line
    else:
        return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

def your_gosperize_with_angle(theta):
    def inner_gosperize(curve_fn):
        
        return put_in_standard_position(connect_ends(rotate(+theta)(curve_fn),
                                                     rotate(-theta)(curve_fn)))
    return inner_gosperize
