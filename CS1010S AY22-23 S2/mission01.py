#
# CS1010S --- Programming Methodology
#
# Mission 1
#
# Note that written answers are commented out to allow us to run your
# code easily while grading your problem set.
# os.chdir("/Users/s/stuff/compro/healtermon/cs1010s/")
from runes import *


##########
# Task 1 #
##########

def mosaic(top_right,bottom_right,bottom_left,top_left):
    return stack( beside(top_left,top_right),
                  beside(bottom_left,bottom_right) )

# Test
# show(mosaic(rcross_bb, sail_bb, corner_bb, nova_bb))
# show(mosaic(heart_bb, pentagram_bb, circle_bb, ribbon_bb))
# show(corner_bb)
##########
# Task 2 #
##########

def simple_fractal(p):
    return beside(p,stack(p,p))

# # Test
# show(simple_fractal(make_cross(rcross_bb)))
# show(simple_fractal(heart_bb))

# show(rcross_bb)
# clear_all()
# show(quarter_turn_right(sail_bb))
# show(turn_upside_down(sail_bb))
# show(quarter_turn_left(sail_bb))
# show(stack(rcross_bb,sail_bb))
# show(stack(rcross_bb,
#            stack(rcross_bb,
#                  sail_bb)))
# show(beside(rcross_bb,sail_bb))
# def make_cross1(pic):
#     return stack(
#         beside(
#             quarter_turn_right(pic),
#             turn_upside_down(pic)),
#         beside(
#             pic,
#             quarter_turn_left(pic)))
    
# show(make_cross1(rcross_bb))
# show(repeat_pattern(5,make_cross,rcross_bb))
# show(stack_frac(1/3, rcross_bb, sail_bb))
# show(stackn(5, nova_bb))
# show(stackn(5, quarter_turn_right(
#     stackn(5, quarter_turn_left(nova_bb)))))


# # stack stack_frac flip_horiz flip_vert beside make_cross
# # quarter_turn_right quarter_turn_left eighth_turn_left turn_upside_down
# # stackn repeat_pattern

# # pics:
# black_bb blank_bb circle_bb heart_bb ribbon_bb pentagram_bb
