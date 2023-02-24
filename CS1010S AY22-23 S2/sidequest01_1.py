from runes import *

def egyptian(p,n):
    """n>=3"""
    row = besiden(n,p)
    col = stackn(n-2,p)
    return stack_frac(1/n,
                      row,
                      stack_frac((n-1-1)/(n-1),
                                 beside_frac(1/n,
                                             col,
                                             beside_frac((n-1-1)/(n-1),p,col)),
                                 row))

def besiden(n, p):
    return quarter_turn_right(stackn(n, quarter_turn_left(p)))

def beside_frac(frac, p1, p2):
    return quarter_turn_right(stack_frac(1-frac,
                                         quarter_turn_left(p2),
                                         quarter_turn_left(p1)))
# show(besiden(5, heart_bb))
# show(egyptian(make_cross(rcross_bb),103))
# show(egyptian(make_cross(rcross_bb), 5))
# show(beside_frac(1/3, heart_bb, pentagram_bb))
