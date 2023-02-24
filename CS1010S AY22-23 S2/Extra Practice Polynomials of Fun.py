def sum(term, a, next, b):
    if (a>b):
        return 0
    else:
        return term(a) + sum(term, next(a), next, b)
def fold(op, f, n):
    if n==0:
        return f(0)
    else:
        return op(f(n), fold(op, f, n-1))
    
def poly(coefs,x):
    return sum(lambda i:coefs[i]*x**i,0,lambda x:x+1,len(coefs)-1)
    
def poly(coefs,x):
    if coefs == (): return 0
    return fold((lambda i,j: i+j),
                (lambda i: coefs[i]*x**i),
                len(coefs)-1)

def filtered_accumulate(op, base, term, a, next, b, filter):
    i, total = a, base
    while i <= b:
        if filter(i):
            total = op(term(i), total)
        i = next(i)
    return total

def poly_acc(coefs,x):
    return filtered_accumulate((lambda i,j: i+j),
                               0,
                               (lambda i: coefs[i]*x**i),
                               0,
                               lambda x:x+1,
                               len(coefs)-1,
                               lambda x:True)
def calculator_generator(coefficients):
    return lambda x: poly(coefficients,x)

def new_poly(coefs,x):
    l = len(coefs)-1
    return filtered_accumulate((lambda i,j: i+j),
                               0,
                               (lambda i: coefs[i]*x**(l-i)),
                               0,
                               lambda x:x+1,
                               l,
                               lambda x:True)
def calculator_generator(coefficients, ptype):
    if ptype=="old": return lambda x: poly(coefficients,x)
    elif ptype=="new":return lambda x: new_poly(coefficients,x)
    else: raise Exception("what did u just input into calculator_generator?")

def generator(ptype):
    if ptype=="old":return lambda x: lambda y: poly(x,y)
    elif ptype=="new":return lambda x: lambda y: new_poly(x,y)
    else: raise Exception("what did u just input into generator?")
