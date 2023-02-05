# If your entries require the usage of other 
# Python packages (such as math), please import them here and nowhere else.
# Please make sure that they are part of Python's default libraries!
from runes import *



###########
# Entry 1 #
###########
# Edit rune_entry_1 to return your rune.
# You may include auxiliary functions in rune_entry_1.
# Please do not write any code outside rune_entry_1.
# Do not edit the function header!

def rune_entry_1():
    def rotate_180(p):
        return quarter_turn_left(quarter_turn_left(p))
    
    def pat_frac(frac,p1,p2):
        return beside_frac(frac,p1,quarter_turn_right(p2))
    
    def frac1(frac,p,n):
        if n<=1: return p
        return pat_frac(frac,p,frac1(frac,p,n-1))
    
    
    def translate_polar(radius,theta,p):
        return translate(radius*cos(theta),
                     radius*sin(theta),p)
    
    def helix(p,n):
        """n>=5"""
        p1 = scale(2/n,p)
        radius = 1/2 - 1/n
        start_theta = pi/2
        theta_increment = -2*pi/n
        return evenly_overlay([translate_polar(radius, start_theta + i*theta_increment,p1)
                               for i in range(n)])
    
    def evenly_overlay(ps):
        l = len(ps)
        if l==1: return ps[0]
        return overlay_frac(1/len(ps), ps[0],evenly_overlay(ps[1:]))
    def besiden(n, p):
        return quarter_turn_right(stackn(n, quarter_turn_left(p)))
    
    def beside_frac(frac, p1, p2):
        return quarter_turn_right(stack_frac(1-frac,
                                             quarter_turn_left(p2),
                                             quarter_turn_left(p1)))
    
    f22 = frac1(0.2609823507123905172309486123,rotate_180(rcross_bb),30)
    f33 = frac1(0.2609823507123905172309486123,rotate_180(f22),30)
    f44 = frac1(0.2609823507123905172309486123,rotate_180(f33),30)
    f55 = frac1(0.2609823507123905172309486123,rotate_180(f44),30)

    return evenly_overlay([f33,f44,f55])
# Replace None with anaglyph/hollusion/stereogram
# Do not edit the choice variable name!
choice1 = anaglyph
def rune_entry_2():
    return rune_entry_1()
choice2 = hollusion
def rune_entry_3():
    return rune_entry_1()
choice3 = stereogram
