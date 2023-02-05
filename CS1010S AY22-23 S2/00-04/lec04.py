def fold2(op, term, a, next, b, base): 
    if a > b:
        return base
    else:
        return op (term(a),
                   fold2(op, term, next(a), next, b, base))
    
def geometric_series(a, r, n):
    return fold2((lambda x,y: x+y),
                 (lambda x: a*r**(x-1)),
                 1,
                 lambda x: x+1,
                 n,
                 0)
def num_combination(n, r):
    """Mathematics' nCr"""
    if r == 0: return 1
    if n==0: return 0
    return num_combination(n-1,r-1) + num_combination(n-1,r)
