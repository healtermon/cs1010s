# TODO: make generalised fractal application function WITH LOOPS
# - then apply rcross_bb with pat_frac (the golden ratio pattern) to get something nice

# from runes_2D import *
from runes import *             # if u import from both runes_2D and runes, tk won't work
from math import *
from mission02 import many_pictures_fractal
from sidequest01_1 import besiden,beside_frac
from mission03 import reduce

def reduce_iter(seq:tuple, bi_or_zero_f, key = identity, initial_value = None, from_end = False):
   a = iter(seq[::-1])
   
# # stack stack_frac flip_horiz flip_vert beside make_cross
# # quarter_turn_right quarter_turn_left eighth_turn_left turn_upside_down
# # stackn besiden repeat_pattern
show(eighth_turn_left(rcross_bb))
# # pics:
# black_bb blank_bb circle_bb heart_bb ribbon_bb pentagram_bb
# blank_bb sail_bb corner_bb spiral_bb rcross_bb nova_bb
def rotate_180(p):
    return quarter_turn_left(quarter_turn_left(p))
golden_ratio = (1 + 5 ** 0.5) / 2
ratio = golden_ratio /(golden_ratio+1)
diagonals_meet = quarter_turn_right(rcross_bb)

def pat_harriss(p1,p2):
    l_to_b = 600/800
    
    return beside_frac(a,
                       quarter_turn_left(p1),
                       stack_frac(b,p2,p3))
def pat_frac(frac,p1,p2):
    return beside_frac(frac,p1,quarter_turn_right(p2))

def frac1(frac,p,n):
    if n<=1: return p
    return pat_frac(frac,p,frac1(frac,p,n-1))



def rune_entry_1():
    return 
def rune_entry_2():
    return
def rune_entry_3():
    return

# show(rune_entry_1()) # Uncomment this to see your rune

# Save rune as png [Optional only if your rune is really complex and large]
# save_image('rune_entry_1') # Uncomment this to save your rune
show(frac1(0.01,rotate_180(rcross_bb),100))
show(frac1(0.260982350712390517230948612360589723849012735902134871286043,rotate_180(rcross_bb),100)) # my favourite ATM
show(frac1(0.2438274,quarter_turn_right(rcross_bb),30))
show(frac1(0.5,quarter_turn_right(rcross_bb),30))

