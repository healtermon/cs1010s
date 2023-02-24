from hi_graph import *
from math import sqrt
# (a)
some_t = 0.5**2
# tupify_point(unit_circle(some_t)) == tupify_point(alternative_unit_circle(0.5))

# (b)
other_t = sqrt(0.09)
# tupify_point(unit_circle(0.09)) == tupify_point(alternative_unit_circle(other_t))

# (c)
t1, t2 = 0.1**2, 0.1
# tupify_point(unit_circle(0.01)) == tupify_point(alternative_unit_circle(0.1))


# (d)
other_t2, other_t1 = 0.90, sqrt(0.90)
# tupify_point(unit_circle(other_t2)) == tupify_point(alternative_unit_circle(other_t1))

def spiral(t):
    return make_point(t**2*sin(2*pi*t**2), t**2*cos(2*pi*t**2))
draw_connected_scaled(1000,spiral)
def heart(t):
    return connect_rigidly(spiral,scale_xy(-1,1)(spiral))(t)
draw_connected_scaled(1000,heart)
