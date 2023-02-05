# TODO: try using other methods https://math.stackexchange.com/questions/130192/method-for-estimating-the-nth-derivative

def f(x):
    return +0*x**0 +0*x**1 +0*x**2 +5*x**3
def g(x):
    return +3*x**1 +5*x**3 -2*x**5 +6*x**6
def h(x):
    return +5*x**0 +1*x**1 +3*x**2 -2*x**11 +3*x**15   

# u are given above functions, go find the coefficients!!!!
# below I create an alternate way of creating functions to test
def polynomial(*coefficients):
    """input should be like polynomial(1,2,3) or polynomial(*[1,2,3]). REMEMBER THE STAR"""
    def f(x):
        sum = 0
        for i in range(len(coefficients)):
            sum += coefficients[i]*x**i
        return sum
    return f


# because I dont know the built-in functions
def pp(x): [print(i) for i in x]
def factorial(x):
    if x==0: return 1
    return x * factorial(x-1)
def identity(x): return x
def ntimes(f,n):
    if n==0: return identity
    return lambda x: ntimes(f,n-1)(f(x))


# ACTUAL SOLUTION STARTS HERE

# I use the simplest derivative-getter, ever.
def deriv(f, h=0.01): # 0.01 or machine epsilon = 7./3 - 4./3 -1 assuming ur com doesn't run on base 3. 0.01 works best for some reason...
    """computes derivative of 1-input function"""
    return lambda x: (f(x+h)-f(x-h))/(2*h)


def subtract(f,a):
    return lambda x: f(x) - a
def subtract_functions(f1,f2):
    return lambda x: f1(x) - f2(x)

def find_polynomial_naive(f):
    """well, was worth a try, it's too slow."""
    pp(map(lambda x: round(ntimes(deriv,x)(f)(0)/factorial(x)),range(100)))

def find_polynomial_naive_2(f):
    """basically the previous one but without recalculating everything"""
    coefficients = []
    for differentiations in range(20):
        powerless_term = f(0)
        pt_rounded = round(powerless_term)
        divisor = factorial(differentiations)
        coefficients += [round(pt_rounded/divisor)]
        # print(f"pt={powerless_term}~~{pt_rounded}, divisor={divisor}")
        f1 = subtract(f, pt_rounded)
        f = deriv(f1)
    print(coefficients)
                
# Deprecated soon, but hey it's in scipy, and allowed to be imported right? 'https://docs.scipy.org/doc/scipy/reference/generated/scipy.misc.derivative.html
# looking at the source code, it calculates central difference weights, so pretty much I don't have to figure out the taylor series math here: https://pythonnumericalmethods.berkeley.edu/notebooks/chapter20.02-Finite-Difference-Approximating-Derivatives.html
from scipy.misc import derivative
def find_polynomial_almost(f):
    """does it up to 15th order(14th power), chokes on huge numbers :("""
    coefficients = []
    for differentiations in range(0,20):
        powerless_term = derivative(f,0,dx=0.01,n=differentiations, order=161)
        pt_rounded = round(powerless_term)
        divisor = factorial(differentiations)
        coefficients += [round(pt_rounded/divisor)]
        # print(f"pt={powerless_term}~~{pt_rounded}, divisor={divisor}")
    print(f"{coefficients}")
        
def find_polynomial_list(f):
    """subtracts away the previously found polynomials, hopefully to reduce noise, seems to help a little."""
    coefficients = []
    for differentiations in range(0,length):
        powerless_term = derivative(subtract_functions(f, polynomial(*coefficients)),0,dx=0.01,n=differentiations, order=161) # order 161, dx=0.01 is best
        pt_rounded = round(powerless_term)
        divisor = factorial(differentiations)
        coefficients += [round(pt_rounded/divisor)]
        # print(f"pt={powerless_term}~~{pt_rounded}, divisor={divisor}")
    print(f"{coefficients}")
    return coefficients
                
# TESTS
length = 16
f0 = polynomial(0,0,0,5)
g0 = polynomial(0,3,0,5,0,-2,6)
h0 = polynomial(5,1,3,0,0,0,0,0,0,0,0,-2,0,0,0,3)
i0 = polynomial(1341,234,512,523,432,512,342,1,5,2,3,7,2,1,3,4,2,5,3,1,2,3)
j0 = polynomial(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)
k0 = polynomial(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
f0d1 = deriv(f0)
h0d1 = deriv(h0)
h0d2 = deriv(h0d1)
j = lambda x: 1*x**15

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

import random
def testThatShit():
    for i in range(50):
        test_list = random.sample(range(-20,20+1),length)
        fun = polynomial(*test_list)
        print(f"Q:{test_list}\nA:",end="")
        result = find_polynomial_list(fun)
        testresult = test_list==result
        if testresult:
            print(f"{color.CYAN}",end="")
        else:
            print(f"{color.RED}",end="")
        print(f"{testresult}")
        print(color.END)


def find_polynomial(f):
    l = find_polynomial_list(f)
    # trim end zeros
    while(l!=[] and l[-1]==0):
        l.pop()
    return tuple(l)
