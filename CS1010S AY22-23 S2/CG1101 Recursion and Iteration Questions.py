from math import sqrt, floor, ceil

def is_prime(n): 
    if n<2: return False
    return not any(i for i in range(2,floor(sqrt(n))+1) if n%i == 0)

def legendre(n):
    return all(any(True for j in range(i**2,(i+1)**2) if is_prime(j))
               for i in range(1,ceil(sqrt(n))))

def legendre_n(n):
    """Returns the number of primes between n**2 and (n+1)**2"""
    return sum(1 for j in range(n**2,(n+1)**2 + 1) if is_prime(j))

def goldbach(n):
    """test Goldbach's Conjecture from 4 till an input n"""
    return all(goldbach_n(i) for i in range(4,n+1,2))
        
def goldbach_n(n):
    """testing goldbach for 1 number n
    There is a commented-out comprehension version below, but they do the same thing:
    - first find the primes from 4 to n
    - for each prime in that list,
      - generate an array of matches with n for that prime + any other prime in the list from that point onwards
    - If any of these returned matches are True(any function), return True"""
    primes = [p for p in range(1,n+1) if is_prime(p)]
    
    # return any(((j,p) for j in primes[start_i:] if j+p == n)
    #            for start_i,p in enumerate(primes))
     
    for start_i,p in enumerate(primes):
        print(f"p:{p}---------")
        for j in primes[start_i:]:
            if j+p == n:
                print(f"{n}={j}+{p}")
                return True

        

def maclaurin(x, n):
    # code that approximates e^x up to the nth term
    return round(sum((x**i)/factorial(i) for i in range(n)),3)
    
def factorial(n):
    if n<=0:return 1
    return n * factorial(n-1)

def conway(n):
    # code that implements Conway's recursive sequence.
    if n<=2: return 1
    return conway(conway(n-1)) + conway(n - conway(n-1))
