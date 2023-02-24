add1 = lambda x : x + 1
identity = lambda x: x
def compose(*fs):
    """used like compose(f1,f2,f3), NOT compose([f1,f2,f3])"""
    def brick_compose(f1=None,f2=None):
        return (lambda x: f1(f2(x))) if f1 and f2 else identity
    return reduce(fs, brick_compose ,initial_value=identity, from_end=True)
def reduce(seq:tuple, bi_or_zero_f, key = identity, initial_value = None, from_end = False):
    """
    Takes in TUPLES
    Like Common Lisp's reduce, but
    Missing start and end optional arguments 'cuz python has neat splicing syntax
    hyperspec: http://www.lispworks.com/documentation/HyperSpec/Body/f_reduce.htm
    """
    def recur(seq):
        if len(seq) == 1: return key(seq[0])
        if from_end:
            return bi_or_zero_f(key(seq[0]),recur(seq[1:]))
        else:
            return bi_or_zero_f(recur(seq[:-1]),key(seq[-1]))
        
    if initial_value:
        if from_end: seq = seq + (initial_value,)
        else:        seq = (initial_value,) + seq
    return recur(seq)


def repeated(f,n):
    return reduce((f,)*n,compose, from_end=True)

def thrice(f):
    return repeated(f,3)
# mission starts here
a = 9

# thrice(thrice)(add1)(6)
# thrice(thrice(thrice(add1)))(6)
# thrice(thrice(add3))(6)
# add27(6)
bi = 33

# thrice(thrice)(identity)(compose)
bii = compose

# sq = lambda x: x*x
# thrice(thrice)(sq)(2)
# thrice(thrice(thrice(sq)))(2)
# thrice(thrice(lambda x: x**(2**3)))(2)
# (lambda x: x**(2**(3**3)))(2)
# 2**(2**(3**3))
# 2**134217728
# sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(sq(2)))))))))))))))))))))))))))
# the number is too big to be displayed.
biii = 2**134217728

def combine(f,op,n):
    result = f(0)
    for i in range(n):
        result = op(result,f(i))
    return result

def smiley_sum(t):
    def f(x): return 2*(x+1)**2
    def op(x,y):
        if x==y: return 1
        return x + y

    n = t
    return combine(f,op,n)

# NECESSARY WORKING, OMG THIS WAS RETARDED TO FIGURE WITHOUT WRITING IT DOWN
# s(1) == op(f(0),f(0)) == 1
# s(2) == op(1, f(1)) == 9
# s(3) == op(9, f(2)) == 27
# s(4) == op(27, f(3)) == 59

# op(f(0),f(0)) == 1
# op(x,f(1)) == x+2*2**2
# op(x,f(2)) == x+2*3**2
# op(x,f(3)) == x+2*4**2
# op(x,f(i)) == x+2*(i+1)**2, where i>0

# pp(map(smiley_sum,range(1,10)))
def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def new_fib(n):
    """I stared at this for 1h before realising this simple solution.
    Coming from the previous problem made it worse. Waste of time."""
    def f(x):
        if x<0: return 0
        else: return fib(x)

    def op(x,y): return y

    return combine(f, op, n+1)


# def combine(f,op,n):
#     """modified combine for helping to think through problem""""
#     result = f(0)
#     for i in range(0,n+1):
#         result = op(result,f(i))
#     return result

# fib(0) == op(op(f(0),f(0)),f(1)) == 0
# fib(1) == op(op(op(f(0),f(0)),f(1)),f(2)) == 1
# fib(2) == ...

# op(op(f(0),f(0)),f(1)) == 0
# op(1, f(2)) == 1                   
# op(1, f(3)) == 1
# op(1, f(4)) == 2 
# op(2, f(5)) == 3 
# op(3, f(6)) == 5 
# op(5, f(7)) == 8
# op(8, f(8)) == 13
# op(13, f(9)) == 21
# op(21, f(10)) == 34 
# op(34, f(11)) == 55 
# op(55, f(12)) == 89
# op(89, f(13)) == 144
