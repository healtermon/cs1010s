# Note: You don't need to submit your tree for coin change for 11 cents in Coursemology.

space_complexity = ""  # Enter the order of growth in space here
time_complexity = ""  # Enter the order of growth in time here


def f(n):
    if n<3: return n
    return f(n-1) + 2*f(n-2) + 3*f(n-3)  

def f1(n):
    if n<3: return 1
    return f1(n-1) + f1(n-2) + f1(n-3)  

def f1(n):
    curr,back1,back2,back3 = 0,1,1,1
    for i in range(3,101):
        curr = back1+back2+back3
        print(f"f({i})={curr}, {round(curr-3**i)}")
        
        back1,back2,back3 = curr,back1,back2
        

[f1(n) - (3**n) for n in range(100)]        
# time_complexity="O(n)"
# space_complexity="O(3**n)"
# use ** to indicate power, without any spaces. For example, O(2**n)


def f(n):
    if n<3: return n
    curr,back1,back2,back3 = 0,2,1,0
    for i in range(3,n+1):
        curr = back1 + 2*back2 + 3*back3
        back3,back2,back1 = back2,back1,curr
    return curr

# time_complexity="O(n)"
# space_complexity="O(1)"
# use ** to indicate power, without spaces, for example O(n**2) to indicate quadratic growth
def fib(n):
    if n<=1: return n
    return fib(n-1) + fib(n-2)

def is_fib(n):
    if 0<=n and n<=3: return True
    curr,back1,back2 = 5,3,2
    while curr<=n:
        print(curr)
        if curr == n: return True
        back1,back2 = curr, back1
        curr = back1 + back2
    return False


# Order of growth in space: O(1)
# Order of growth in time: O(log(n))
# test:
# [is_fib(n) for n in [fib(n) for n in range(20)]]


from math import *

def make_fare(stage1, stage2, start_fare, increment, block1, block2):
    # copy taxi_fare inside here
    def taxi_fare(distance): #distance in metres
        if distance <= stage1:
            return start_fare
        elif distance <= stage2:
            return start_fare + (increment*ceil((distance - stage1) / block1))
        else:
            return taxi_fare(stage2) + (increment*ceil((distance - stage2) / block2))
    # Returns a function that calculates the taxi fare using the values given
    return taxi_fare

#DO NOT REMOVE THIS LINE
comfort_fare = make_fare(1000, 10000, 3.0, 0.22, 400, 350) 

