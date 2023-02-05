from hi_graph import *
    

# draw_points(200, unit_circle) # dots along top-right of circle
# draw_points_scaled(200, unit_circle) # dots along circle
# draw_connected(200, unit_circle) # connected top-right of circle
# draw_connected_scaled(200, unit_circle) # connected circle

# a: ambiguous question, can it be out of screen? Yes right?
# unit_line_at_y(Number) -> Curve
# b: a_line(Unit-Interval) -> Point
# c:
def vertical_line(point,length):
    if length<0: raise Exception("Nah uh uh, what does negative length mean? of course it means to draw the other way, duh! wait...no! The question doesn't allow it!")
    return lambda t: make_point(x_of(point), length*t + y_of(point))

# draw_points(200, vertical_line(make_point(0.1,0.2), 0.11))
# y_of((vertical_line(make_point(0.1,0.2), 0.11))(0.5))

# d: vertical_line(Point,Number) -> Curve
# e:
draw_connected(2,vertical_line(make_point(0.5,0.25),0.5))

# task 2
# test it on a curve that is not symmetric about the y-axis and changes value with increasing y in viewable range(0<=x<=1, 0<=y<=1), then apply reflect_through_y_axis and translate it back into view, like using the function test_reflection_function below. Compare the before and after, put the 2 windows generated side by side and see if the curves reflect each other.
def reflect_through_y_axis(curve):
    return lambda t: make_point(-x_of(curve(t)),y_of(curve(t)))
def reflect_viewable_curve_through_y_axis_and_translate_back_into_view(curve):
    curve = reflect_through_y_axis(curve)
    return lambda t: make_point(1 + x_of(curve(t)),y_of(curve(t)))
def test_curve(t):
    from math import exp
    return make_point(t,exp(-2*t))
def test_reflection_function():
    draw_connected(200,test_curve)
    draw_connected(200,reflect_viewable_curve_through_y_axis_and_translate_back_into_view(test_curve))
