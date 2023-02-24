#################################
# Tidy version of runes_2D.py   #
# Last updated: 4 May 2022      #
#################################

########### START OF SETUP ###########

# Constants
viewport_size = 600 # This is the height of the viewport
spread = 20
active_hollusion = None
lastframe = None

import graphics
import math
import time
import PyGif

Posn = graphics.Posn
Rgb = graphics.Rgb
draw_solid_polygon = graphics.draw_solid_polygon

graphics.init(viewport_size)
vp = graphics.open_viewport("ViewPort", 4/3 * viewport_size, viewport_size)
lp = graphics.open_pixmap("LeftPort", 4/3 * viewport_size, viewport_size)
rp = graphics.open_pixmap("RightPort", 4/3 * viewport_size, viewport_size)

def is_list(lst):
    """
    A setup function to check for types. Nothing to see here.
    """
    
    return isinstance(lst, (list, tuple))

class Frame:
    """
    A frame object. Nothing to see here.
    """

    def __init__(self, p0, p1, p2, z1, z2):
        self.orig = p0
        self.x = p1
        self.y = p2
        self.z1 = z1
        self.z2 = z2

unit_frame = Frame(
    Posn(1/6 * viewport_size, 0),
    Posn(viewport_size,0),
    Posn(0,viewport_size),
    0, 1)

def scale_vect(mult, p):
    """
    A setup function to scale vectors. Nothing to see here.
    """

    return Posn(mult*p.x, mult*p.y)

def transform_posn(frame):
    """
    A setup function for position transformation. Nothing to see here.
    """
    
    def f(posn):
        return frame.orig + (scale_vect(posn.x/viewport_size, frame.x) + scale_vect(posn.y/viewport_size, frame.y))
    return f

def inverse_transform_posn(frame):
    """
    The 'inverse' of transform_posn. Nothing to see here.
    """
    
    a = frame.x.x
    b = frame.y.x
    c = frame.x.y
    d = frame.y.y
    det = a*d - b*c
    
    if det == 0:
        raise Exception("somehow you managed to zero the determinant for your frame")
    inv_mat = ((d/det, -b/det), (-c/det, a/det))
    
    def function(posn):
        nonlocal inv_mat
        t = list(map(lambda m: m[0] * (posn.x - frame.orig.x) + m[1] * (posn.y - frame.orig.y), inv_mat))
        return Posn(viewport_size*t[0], viewport_size*t[1])
    return function

def center_and_fill(p):
    """
    A function used in circle_bb, spiral_bb, and ribbon_bb. Nothing to see here.
    """

    center = Posn(viewport_size / 2, viewport_size / 2)
    return center + scale_vect(viewport_size / 2, p)

############ END OF SETUP ############

def show(painter):
    """
    Shows the painter at the working window.
    """

    return painter(vp, unit_frame)

def clear_all():
    """
    Clears the current working window.
    """

    global active_hollusion
    global vp, lp, rp
    if active_hollusion != None:
        active_hollusion("kill")
        active_hollusion = None
    graphics.clear_viewport(vp)
    graphics.clear_viewport(lp)
    graphics.clear_viewport(rp)

def blank_bb(vp, frame):
    """
    A blank rune. Basically nothing.
    """
    
    return

def sail_bb(vp, frame):
    """
    A sail-shaped rune.
    """

    p = [Posn(viewport_size / 2, 0), Posn(viewport_size / 2, viewport_size), Posn(viewport_size, viewport_size)]
    if is_list(vp[0]):
        for count, port in enumerate(vp):
            draw_solid_polygon(port, map(transform_posn(frame), p),
                Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),
                Rgb(frame.z1, frame.z1, frame.z1))
    elif vp != None:
        draw_solid_polygon(vp, map(transform_posn(frame), p), Posn(0, 0), Rgb(frame.z1, frame.z1, frame.z1))

def corner_bb(vp, frame):
    """
    A small triangular rune at the corner.
    """

    p = [Posn(viewport_size / 2, 0), Posn(viewport_size, 0), Posn(viewport_size, viewport_size / 2)]
    if is_list(vp[0]):
        for count, port in enumerate(vp):
            draw_solid_polygon(port, map(transform_posn(frame), p),
                Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),
                Rgb(frame.z1, frame.z1, frame.z1))
    elif vp != None:
        draw_solid_polygon(vp, map(transform_posn(frame), p), Posn(0, 0), Rgb(frame.z1, frame.z1, frame.z1))

def black_bb(vp, frame):
    """
    A rune without any blank space.
    """

    p = [Posn(0, 0), Posn(viewport_size, 0), Posn(viewport_size, viewport_size), Posn(0, viewport_size)]
    if is_list(vp[0]):
        for count, port in enumerate(vp):
            draw_solid_polygon(port, map(transform_posn(frame), p),
                Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),
                Rgb(frame.z1, frame.z1, frame.z1))
    elif vp != None:
        draw_solid_polygon(vp, map(transform_posn(frame), p), Posn(0, 0), Rgb(frame.z1, frame.z1, frame.z1))

def spiral_bb(vp, frame):
    """
    A rune that definitely looks like a spiral.
    """

    theta_max = 30
    offset = 0.1
    angle = 0
    p = []
    while angle < theta_max:
        p.append(Posn((offset + angle/theta_max) * math.cos(angle), (offset + angle/theta_max) * math.sin(angle)))
        angle += offset
    if is_list(vp[0]):
        for count, port in enumerate(vp):
            draw_solid_polygon(port, map(transform_posn(frame), map(center_and_fill, p)),
                Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),
                Rgb(frame.z1, frame.z1, frame.z1))
    elif vp != None:
        draw_solid_polygon(vp, map(transform_posn(frame), map(center_and_fill, p)), Posn(0, 0), Rgb(frame.z1, frame.z1, frame.z1))

def circle_bb(vp, frame):
    """
    A perfect circle rune!
    """

    unit = 50
    p = []
    angle = 0
    while angle < 2 * math.pi:
        p.append(Posn(math.cos(angle), math.sin(angle)))
        angle += unit / viewport_size
    if is_list(vp[0]):
        for count, port in enumerate(vp):
            draw_solid_polygon(port, map(transform_posn(frame), map(center_and_fill, p)),
                Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),
                Rgb(frame.z1, frame.z1, frame.z1))
    elif vp != None:
        draw_solid_polygon(vp, map(transform_posn(frame), map(center_and_fill, p)), Posn(0, 0), Rgb(frame.z1, frame.z1, frame.z1))

def pentagram_bb(vp, frame):
    """
    A star-shaped rune. How cool is that?
    """

    unit_offset = viewport_size / 2
    s1 = math.sin(2 * math.pi / 5) * unit_offset
    c1 = math.cos(2 * math.pi / 5) * unit_offset
    s2 = math.sin(4 * math.pi / 5) * unit_offset
    c2 = math.cos(math.pi / 5) * unit_offset
    a = s2 / (s1 + s2)
    a_ = 1 - a
    p = [
        Posn(-s1 + unit_offset, -c1 + unit_offset),
        Posn(s1 + unit_offset, -c1 + unit_offset),
        Posn(-s2 + unit_offset, c2 + unit_offset),
        Posn(unit_offset, 0),
        Posn(s2 + unit_offset, c2 + unit_offset)
    ]

    p = [
        p[0], p[3] * a + p[2] * a_,
        p[2], p[1] * a + p[2] * a_,
        p[4], p[2] * a + p[1] * a_,
        p[1], p[4] * a + p[3] * a_,
        p[3], p[2] * a + p[3] * a_
    ]

    if is_list(vp[0]):
        for count, port in enumerate(vp):
            draw_solid_polygon(port, map(transform_posn(frame), p),
                Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),
                Rgb(frame.z1, frame.z1, frame.z1))
    elif vp != None:
        draw_solid_polygon(vp, map(transform_posn(frame), p), Posn(0, 0), Rgb(frame.z1, frame.z1, frame.z1))

def heart_bb(vp, frame):
    """
    A heart-shaped rune. Good to spread positivity :)
    """

    k = math.sqrt(2) / 2
    p = [
        Posn(viewport_size / 2, (1 - k) / (1 + 3*k) * viewport_size),
        Posn((1 - k) / (1 + k) * viewport_size / 2, (1 + k) / (1 + 3*k) * viewport_size),
        Posn(viewport_size / 2, viewport_size),
        Posn(viewport_size - (1 - k) / (1 + k) * viewport_size / 2, (1 + k) / (1 + 3*k) * viewport_size)
    ]

    # Draws a kite
    if is_list(vp[0]):
        for count, port in enumerate(vp):
            draw_solid_polygon(port, map(transform_posn(frame), p),
                Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),
                Rgb(frame.z1, frame.z1, frame.z1))
    elif vp != None:
        draw_solid_polygon(vp, map(transform_posn(frame), p), Posn(0, 0), Rgb(frame.z1, frame.z1, frame.z1))
    
    # Draws the top of the heart
    heart_circle = stack_frac(
        2 / (1 + 3 * k),
        quarter_turn_right(
            stack_frac(k / (1 + k), blank_bb, circle_bb)
        ),
        blank_bb)
    heart_circle(vp, frame)
    flip_horiz(heart_circle)(vp, frame)

def rcross_bb(vp, frame):
    """
    An upper triangular rune with some small part mirrored to its diagonal.
    """

    p1 = [
        Posn(0, 0),
        Posn(viewport_size / 4, viewport_size / 4),
        Posn(3 * viewport_size / 4, viewport_size / 4),
        Posn(3 * viewport_size / 4, 3 * viewport_size / 4),
        Posn(viewport_size, viewport_size),
        Posn(viewport_size, 0)
    ]
    
    p2 = [
        Posn(viewport_size / 4, viewport_size / 4),
        Posn(viewport_size / 4, 3 * viewport_size / 4),
        Posn(3 * viewport_size / 4, 3 * viewport_size / 4)
    ]

    if is_list(vp[0]):
        for count, port in enumerate(vp):
            draw_solid_polygon(port, map(transform_posn(frame), p1),
                Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),
                Rgb(frame.z1, frame.z1, frame.z1))
            draw_solid_polygon(port, map(transform_posn(frame), p2),
                Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),
                Rgb(frame.z1, frame.z1, frame.z1))
    elif vp != None:
        draw_solid_polygon(vp, map(transform_posn(frame), p1), Posn(0, 0), Rgb(frame.z1, frame.z1, frame.z1))
        draw_solid_polygon(vp, map(transform_posn(frame), p2), Posn(0, 0), Rgb(frame.z1, frame.z1, frame.z1))

def ribbon_bb(vp, frame):
    """
    A ribbon-shaped rune, similar to a beautiful spiral.
    """

    theta_max = 30
    thickness = -1 / theta_max
    unit = 0.1
    p = []
    angle = 0
    
    # Make ribbon
    while angle < theta_max:
        p.append(Posn((angle / theta_max) * math.cos(angle), (angle / theta_max) * math.sin(angle)))
        angle += unit
    
    # Close it
    while angle > 0:
        p.append(Posn(
            abs(math.cos(angle) * thickness) + (angle / theta_max * math.cos(angle)),
            abs(math.sin(angle) * thickness) + (angle / theta_max * math.sin(angle))
        ))
        angle -= unit
    
    if is_list(vp[0]):
        for count, port in enumerate(vp):
            draw_solid_polygon(port, map(transform_posn(frame), map(center_and_fill, p)),
                Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),
                Rgb(frame.z1, frame.z1, frame.z1))
    elif vp != None:
        draw_solid_polygon(vp, map(transform_posn(frame), map(center_and_fill, p)), Posn(0, 0), Rgb(frame.z1, frame.z1, frame.z1))

def nova_bb(vp, frame):
    """
    Two small sail-shaped runes combined into an L-shaped rune.
    """

    p = [
        Posn(viewport_size / 2, 0),
        Posn(viewport_size / 4, viewport_size / 2),
        Posn(viewport_size, viewport_size / 2),
        Posn(viewport_size / 2, viewport_size / 4)
    ]

    if is_list(vp[0]):
        for count, port in enumerate(vp):
            draw_solid_polygon(port, map(transform_posn(frame), p),
                Posn((0.3 - frame.z1) * (spread * (((2 * count) / (len(vp) - 1)) - 1)), 0),
                Rgb(frame.z1, frame.z1, frame.z1))
    elif vp != None:
        draw_solid_polygon(vp, map(transform_posn(frame), p), Posn(0, 0), Rgb(frame.z1, frame.z1, frame.z1))

# Frame transformation factory
def process_frame(op, frame):
    """
    A frame transformation factory. Nothing to see here.
    """
    
    p0 = frame.orig
    p1 = frame.x
    p2 = frame.y
    z1 = frame.z1
    z2 = frame.z2

    if (op == "bottom_frac"):
        return lambda frac: Frame(p0 + scale_vect(1 - frac, p2), p1, scale_vect(frac, p2), z1, z2)
    elif (op == "top_frac"):
        return lambda frac: Frame(p0, p1, scale_vect(frac, p2), z1, z2)
    # To devs, probably unused
    elif (op == "left"):
        return Frame(p0, scale_vect(1/2, p1), p2, z1, z2)
    # To devs, probably unused
    elif (op == "right"):
        return Frame(p0 + scale_vect(1/2, p1), scale_vect(1/2, p1), p2, z1, z2)
    elif (op == "flip_horiz"):
        return Frame(p0 + p1, scale_vect(-1, p1), p2, z1, z2)
    elif (op == "flip_vert"):
        return Frame(p0 + p2, p1, scale_vect(-1, p2), z1, z2)
    elif (op == "reduce_2"): # unused in original
        raise NotImplementedError("reduce_2 is not implemented")
    elif (op == "rotate"): 
        def function(rad):
            cos_theta = math.cos(rad)
            sin_theta = math.sin(rad)
            def rotate_posn(p):
                return Posn(cos_theta * p.x + sin_theta * p.y, cos_theta * p.y - sin_theta * p.x)
            half_gradient = scale_vect(1/2, p1 + p2)
            center = p0 + half_gradient + rotate_posn(scale_vect(-1, half_gradient))
            return Frame(center, rotate_posn(p1), rotate_posn(p2), z1, z2)
        return function
    elif (op == "rotate90"):
        return Frame(p0 + p1, p2, scale_vect(-1, p1), z1, z2)
    elif (op == "deep_frac"):
        return lambda frac: Frame(p0, p1, p2, z1 + ((z2 - z1) * frac), z2)
    elif (op == "shallow_frac"):
        return lambda frac: Frame(p0, p1, p2, z1, z1 + ((z2 - z1) * frac))
    elif (op == "scale_independent"):
        def function(ratio_x, ratio_y):
            d_xy = (p1 * (1 - ratio_x) + p2 * (1 - ratio_y)) * 0.5
            center = p0 + d_xy
            return Frame(center, p1 * ratio_x, p2 * ratio_y, z1, z2)
        return function
    elif (op == "translate"): 
        return lambda x,y: Frame(p0 + scale_vect(x, p1) + scale_vect(y, p2), p1, p2, z1, z2)

# Basic painter combinations
def stack_frac(frac, p1, p2):
    """
    Stacks p1 on top and p2 on bottom with the vertical proportion of p1 equals frac.
    """
    
    def function(vp, frame):
        if not 0 <= frac <= 1:
            raise ValueError("stack_frac: 0 <= frac <= 1 is required")
        else:
            uf = process_frame("top_frac", frame)(frac)
            lf = process_frame("bottom_frac", frame)(1 - frac)
            p1(vp, uf)
            p2(vp, lf)
    return function

def stack(p1, p2):
    """
    Stacks p1 on top and p2 on bottom with equal proportion.
    """

    return stack_frac(1/2, p1, p2)

def rotate(rad, painter):
    """
    Rotate a rune by a certain angle, in radians.
    """
    
    def function(vp, frame):
        painter(vp, process_frame("rotate", frame)(rad))
    return function

def eighth_turn_left(painter):
    """
    Rotate a rune by pi/4 radians counterclockwise.
    In other words, 45 degrees to the left.
    """

    return rotate(math.pi/4, painter)

def quarter_turn_right(painter):
    """
    Rotate a rune by pi/2 radians clockwise.
    In other words, 90 degrees to the right.
    """

    def function(vp, frame):
        painter(vp, process_frame("rotate90", frame))
    return function

def flip_vert(painter):
    """
    Flips a rune vertically.
    """
    
    def function(vp, frame):
        painter(vp, process_frame("flip_vert", frame))
    return function


def flip_horiz(painter):
    """
    Flips a rune horizontally.
    """
    
    def function(vp, frame):
        painter(vp, process_frame("flip_horiz", frame))
    return function

def scale_independent(ratio_x, ratio_y, painter):
    """
    Scales a rune's width by ratio_x and its height by ratio_y.
    The scaling anchor point is the center of the rune.
    """

    def function(vp, frame):
        painter(vp, process_frame("scale_independent", frame)(ratio_x, ratio_y))
    return function

def scale(ratio, painter):
    """
    Scales a rune by a ratio, maintaining aspect ratio.
    """
    
    return scale_independent(ratio, ratio, painter)

def translate(x, y, painter):
    """
    Translates a rune by x * 100% of the screen to the right and by y * 100% of the screen downwards.
    Positive x means to the right, positive y means downwards.
    """
    
    def function(vp, frame):
        painter(vp, process_frame("translate", frame)(x, y))
    return function

def turn_upside_down(painter):
    """
    Turns a rune upside down, a.k.a. 180 degrees.
    """

    return quarter_turn_right(quarter_turn_right(painter))

def quarter_turn_left(painter):
    """
    Turns a rune to the left by 90 degrees.
    In other word, pi/2 radians counterclockwise.
    """
    
    return turn_upside_down(quarter_turn_right(painter))

def beside(painter1, painter2):
    """
    Puts painter1 and painter2 beside each other.
    Both runes share the same horizontal proportion.
    """

    return quarter_turn_right(stack(quarter_turn_left(painter2), quarter_turn_left(painter1)))

def make_cross(painter):
    """
    Creates a cross out of the base rune.
    """
    
    return stack(beside(quarter_turn_right(painter), turn_upside_down(painter)), beside(painter,quarter_turn_left(painter)))

def repeat_pattern(n, pat, pic):
    """
    Repeats a pattern, pat, on a rune, pic, by n times.
    """

    if n == 0:
        return pic
    else:
        return pat(repeat_pattern(n-1, pat, pic))

def stackn(n, painter):
    """
    Stacks n identical runes vertically.
    The vertical proportions of the runes will be all equal.
    """
    
    if n == 1:
        return painter
    else:
        return stack_frac(1/n, painter, stackn(n-1, painter))

from random import random

def save_image(filename):
    """
    Saves a rune into an image file.
    """
    
    graphics.saveImage(vp, filename)