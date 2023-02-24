from runes import *
from mission01 import mosaic

def pat(p1,p2,p3):
    return stack(p1,beside(p2,p3))

def is_odd(x):return x%2

# this way generalises to other possible patterns, instead of stack_frac + besiden way where it's only top-down
def toggle_fractal(ip1,ip2, n, layer=1):
    p = ip1 if is_odd(layer) else ip2
    if layer>=n: return p
    p1 = toggle_fractal(ip1,ip2,n,layer+1)
    return pat(p,p1,p1)

def fractal(p,n):
    def pat(p1,p2,p3): return stack(p1,beside(p2,p3))

    if n<=1: return p
    return pat(p,fractal(p,n-1),fractal(p,n-1))

def fractal_better(p,n): return toggle_fractal(p,p,n)

def dual_fractal(p1,p2,n):
    """
    recursive procedure that generates a recursive process, generates
    runes p1 on odd layers and p2 on even layers.
    Because I'm stuck with these parameters, whether it is odd
    or even is encoded in positive/negative n number. Another way is to swap p1 and p2 everytime u call it.
    The magnitude of n shows number of layers left.
    """
    def pat(p1,p2,p3): return stack(p1,beside(p2,p3))

    p = p1 if n>0 else p2
    if abs(n)<=1: return p
    next_n = -(n-1 if n>0 else n+1)
    return pat(p,dual_fractal(p1,p2,next_n),dual_fractal(p1,p2,next_n))
    
def many_pictures_fractal(ps,n,p_index=0):
    """generalised version of toggle_fractal
    ps should be an iterable of pictures to go through in layers, n is number of layers left,
    p_index is index of current picture to display of ps at this layer"""
    p = ps[p_index]
    if n<=1: return p
    p1 = many_pictures_fractal(ps,n-1,(p_index+1)%len(ps))
    return pat(p,p1,p1)

def dual_fractal_mutual_recursion(p1,p2,n):
    def pat(p1,p2,p3): return stack(p1,beside(p2,p3))
    def fractal(n): return p1 if n<=1 else pat(p1, latcarf(n-1),latcarf(n-1))
    def latcarf(n): return p2 if n<=1 else pat(p2, fractal(n-1),fractal(n-1))

    return fractal(n)

def dual_fractal_better(p1,p2,n): return toggle_fractal(p1,p2,n)
def dual_fractal_even_better(p1,p2,n): return many_pictures_fractal([p1,p2],n)

def fractal_iter(p,n):
    p1 = p
    for n in range(n-1):
        p1 = pat(p,p1,p1)
    return p1

def dual_fractal_iter(odd_p,even_p,n):
    p = odd_p if is_odd(n) else even_p
    for layer in range(1,n)[::-1]:
        p = pat(odd_p if is_odd(layer) else even_p,
                p,
                p)
    return p


# show(fractal(make_cross(rcross_bb), 4))
# show(dual_fractal(make_cross(rcross_bb), make_cross(nova_bb), 4))


# show(hollusion(nova_bb))
def evenly_overlay(ps):
    l = len(ps)
    if l==1: return ps[0]
    return overlay_frac(1/len(ps), ps[0],evenly_overlay(ps[1:]))

def steps(top_right,bottom_right,bottom_left,top_left):
    b = blank_bb
    return evenly_overlay(mosaic(*args) for args in [[b,b,b,top_left],
                                                     [b,b,bottom_left,b],
                                                     [b,bottom_right,b,b],
                                                     [top_right,b,b,b]])
# show(steps(rcross_bb, sail_bb, corner_bb, nova_bb))    
