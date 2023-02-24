from hi_graph_connect_ends import *
from diagnostic import *
from math import pi

##########
# Task 1 #
##########

# -------------
# gosper_curve:
# -------------
def gosperize(curve):
    scaled_curve = scale(sqrt(2)/2)(curve)
    left_curve = rotate(pi/4)(scaled_curve)
    right_curve = translate(0.5,0.5)(rotate(-pi/4)(scaled_curve))
    return connect_rigidly(left_curve, right_curve)
def gosper_curve(level): return repeated(gosperize, level)(unit_line)

profile_fn(lambda:gosper_curve(10)(0.5),100000) # 2105, 0.02105
profile_fn(lambda:gosper_curve(100)(0.5),10000) # 2697, 0.2697
profile_fn(lambda:gosper_curve(500)(0.5),1000) # 1714, 1.714
profile_fn(lambda:gosper_curve(1000)(0.5),1000) # 3610, 3.610
profile_fn(lambda:gosper_curve(1000)(0.25), 10000) # 35887, 3.5887
# profile_fn(lambda:gosper_curve(10000)(0.5),100) # Process Python segmentation fault: 11

# ------------------------
# gosper_curve_with_angle:
# ------------------------
def gosperize_with_angle(theta):
    def inner_gosperize(curve):
        scale_factor = (1 / cos(theta)) / 2
        scaled_curve = scale(scale_factor)(curve)
        left_curve = rotate(theta)(scaled_curve)
        right_curve = translate(0.5,sin(theta)*scale_factor)(rotate(-theta)(scaled_curve))
        return connect_rigidly(left_curve, right_curve)
    return inner_gosperize

def gosper_curve_with_angle(level, angle_at_level):
    if level == 0: return unit_line
    return gosperize_with_angle(angle_at_level(level))(gosper_curve_with_angle(level-1, angle_at_level))

angle = pi/4
angle_fn = lambda lvl: angle
profile_fn(lambda:gosper_curve_with_angle(10,angle_fn)(0.5),100000)    # 2082  0.02082
profile_fn(lambda:gosper_curve_with_angle(100,angle_fn)(0.5),10000)    # 2692  0.2692
profile_fn(lambda:gosper_curve_with_angle(500,angle_fn)(0.5),1000)     # 1557  1.557
profile_fn(lambda:gosper_curve_with_angle(1000,angle_fn)(0.5),1000)    # 3421  3.421
profile_fn(lambda:gosper_curve_with_angle(1000,angle_fn)(0.25), 10000) # 34290 3.4290


# -----------------------------
# your_gosper_curve_with_angle:
# -----------------------------
def your_gosperize_with_angle(theta):
    return lambda curve_fn: put_in_standard_position(connect_ends(rotate(+theta)(curve_fn),
                                                             rotate(-theta)(curve_fn)))
def your_gosper_curve_with_angle(level, angle_at_level):
    if level == 0: return unit_line
    return your_gosperize_with_angle(angle_at_level(level))(your_gosper_curve_with_angle(level-1, angle_at_level))

profile_fn(lambda:your_gosper_curve_with_angle(10,angle_fn)(0.5),10000)  # 4793  0.04793
profile_fn(lambda:your_gosper_curve_with_angle(100,angle_fn)(0.5),1000)  # 47216 4.7216 
profile_fn(lambda:your_gosper_curve_with_angle(500,angle_fn)(0.5),10)    # 11925 1192.5
profile_fn(lambda:your_gosper_curve_with_angle(1000,angle_fn)(0.5),10)   # 47651 4765.1
profile_fn(lambda:your_gosper_curve_with_angle(1000,angle_fn)(0.25), 10) # 47396 4739.6

# here it is in a table, much easier to read:
# | function_name                | level |   t | times run | time taken(ms) | average time taken(ms) |
# |------------------------------+-------+-----+-----------+----------------+------------------------|
# | profile_fn                   |    10 |  .5 |    100000 |           2105 |                0.02105 |
# | gosper_curve_with_angle      |    10 |  .5 |    100000 |           2082 |                0.02082 |
# | your_gosper_curve_with_angle |    10 |  .5 |     10000 |           4793 |                0.04793 |

# | profile_fn                   |   100 |  .5 |     10000 |           2697 |                 0.2697 |
# | gosper_curve_with_angle      |   100 |  .5 |     10000 |           2692 |                 0.2692 |
# | your_gosper_curve_with_angle |   100 |  .5 |      1000 |          47216 |                 4.7216 |

# | profile_fn                   |   500 |  .5 |      1000 |           1714 |                  1.714 |
# | gosper_curve_with_angle      |   500 |  .5 |      1000 |           1557 |                  1.557 |
# | your_gosper_curve_with_angle |   500 |  .5 |        10 |          11925 |                 1192.5 |

# | profile_fn                   |  1000 |  .5 |      1000 |           3610 |                  3.610 |
# | gosper_curve_with_angle      |  1000 |  .5 |      1000 |           3421 |                  3.421 |
# | your_gosper_curve_with_angle |  1000 |  .5 |        10 |          47651 |                 4765.1 |

# | profile_fn                   |  1000 | .25 |     10000 |          35887 |                 3.5887 |
# | gosper_curve_with_angle      |  1000 | .25 |     10000 |          34290 |                 3.4290 |
# | your_gosper_curve_with_angle |  1000 | .25 |       100 |          47396 |                 4739.6 |

# clearly, this isn't a fair test for customisability of functions. Each of the functions calculate gosper curves differently. We can therefore conclude nothing of that sort. Yay!
# However, logically, a more customised recursive function (without tail recursion with tail-call-optimisation) will incur a deeper call stack and allocate memory for more variables, so it should slow down the code a little.
# Creating iterative functions will get rid of this problem though. For constants, the compiler should optimise the variable allocation away by substituting in the literal so it doesn't matter in the end.
# Between gosper_curve and gosper_curve_with_angle, the former is less customisable and slower. This is likely due to the differing way of calculating gosper curves.
# Between gosper_curve_with_angle and your_gosper_curve_with_angle, clearly your_gosper_curve_with_angle is much slower, the difference being in the gosperize_with_angle functions.
#  The latter is clearly much more computationally expensive based on the benchmarks.
# The exercise seems to want to say "It depends; how you calculate the function is likely going to slow down your code more than adding customisability to the function, so don't think too much of it.
# Besides, more customisability = more code reuse, which may be suitable depending on the situation"

##########
# Task 2 #
##########
#  1) yes
#  2) If you stack a bunch of these curves called on each other (which is what I
#  think "linear/exponential in the level" means, what a vague question!), with
#  the former definition, each calculation of the current level of curve would
#  call 1 of the (level-1) curve of the same kind, while for the latter it calls
#  2. Hence the difference is O(level) vs O(level**2), which is linear vs
#  exponential process, as asked of the qn.

##########
# Task 3 #
##########

def fib(n): return n if n<2 else fib(n-1)+fib(n-2)
trace(fib)
fib(3)


trace(x_of)
gosper_curve(1)(0.5)
gosper_curve(2)(0.5)
gosper_curve(3)(0.5)
gosper_curve(4)(0.5)
gosper_curve(5)(0.5)

def joe_rotate(angle):
    def transform(curve):
        def rotated_curve(t):
            x, y = x_of(curve(t)), y_of(curve(t))
            cos_a, sin_a = cos(angle), sin(angle)
            return make_point(cos_a*x - sin_a*y, sin_a*x + cos_a*y)
        return rotated_curve
    return transform

original_rotate = rotate
replace_fn(rotate, joe_rotate)
gosper_curve(1)(0.5)
gosper_curve(2)(0.5)
gosper_curve(3)(0.5)
gosper_curve(4)(0.5)
gosper_curve(5)(0.5)

replace_fn(joe_rotate,original_rotate)

# | level | rotate | joe_rotate |
# |-------+--------+------------|
# |     1 |      3 |          3 |
# |     2 |      5 |          7 |
# |     3 |      7 |         15 |
# |     4 |      9 |         30 |
# |     5 |     12 |         62 |

#  Evidence of exponential growth in joe_rotate.

