from mission02 import is_odd

def calc_integral(f, a, b, n):
    h = (b-a)/n
    
    sum = 0
    for k in range(n+1):
        if k==0 or k==n: coef = 1
        elif is_odd(k): coef = 4
        else: coef = 2
        sum += coef * f(a + k*h)
    sum *= h/3
    return sum

def fold(op, f, n):
    if n == 0:
        return f(0)
    return op(f(n), fold(op, f, n-1))

def g(k):
    return fold((lambda x,y:x*y),(lambda x: x-(x+1)**2),k)

# print(g(0))
# print(g(8))


def accumulate(combiner,base,term,a,next,b):
    if a>b: return base
    return combiner(term(a),accumulate(combiner,base,term,next(a),next,b))

def sum(term, a, next, b):
    return accumulate((lambda x,y: x+y),0,term,a,next,b)

def accumulate_iter(combiner, null_value, term, a, next, b):
    a_n = []
    while a<=b:
        a_n.append(term(a))
        a = next(a)
    acc = null_value
    for t in a_n[::-1]:
        acc = combiner(t,acc)
    return acc



def make_point(x, y): return (x,y)
def x_point(p): return p[0]
def y_point(p): return p[1]

def make_segment(p1, p2): return (p1,p2)
def start_segment(s): return s[0]
def end_segment(s): return s[1]

def midpoint_segment(segment):
    def avg(x,y):return (x+y)/2
    return make_point(avg(x_point(start_segment(segment)),x_point(end_segment(segment))),
                      avg(y_point(start_segment(segment)),y_point(end_segment(segment))))

# Your rectangle constructor here
def rect(top_left,size):
    # like in C#
    return (top_left,size)

# Add any selector functions and other functions if you need here
#####################################
def top_left(rect): return rect[0]
def size(rect): return rect[1]
#####################################

# Complete the implementation of perimeter and area
def perimeter(rect):
    s = size(rect)
    return 2*(x_point(s) + y_point(s))

def area(rect):
    s = size(rect)
    return x_point(s)*y_point(s)

# Construct a rectangle of length 5 and width 3
rect_a = rect(make_point(0,0),make_point(5,3))

# Construct a rectangle of length 4 and width 7
rect_b = rect(make_point(0,0),make_point(4,7))
