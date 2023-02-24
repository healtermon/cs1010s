from runes import *
from math import sin,cos,pi
from mission02 import evenly_overlay

show(overlay((scale(1/4,circle_bb), blank_bb)))
show((translate(1/2,1/4,scale(1/4,circle_bb))))
show(tree(4,circle_bb))
show(helix(circle_bb,8))
show(helix(make_cross(rcross_bb),9))
show(anaglyph(helix(make_cross(rcross_bb),9)))
def tree(n,p):
    p1 = p
    for i in range(2,n+1):
        p1 = overlay_frac(1/i,scale((n+1-i)/n,p),p1)
    return p1

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
