from math import *

def exception_function(f, rejected_input, new_output):
    return lambda x: f(x) if x != rejected_input else new_output

def usually_double(x): return x*2
def new_double(x):
    return exception_function(exception_function(exception_function(usually_double,4,0),7,0),11,0)(x)

def make_generator(op):
    return lambda y: (lambda x: op(x,y))
