def help(i):
    if type(i) is not int or i<=0: return None
    return (i//100)%10
def get_hundredth(*args):
    return tuple(help(arg) for arg in args)
        

def avg(tup):
    return sum(tup)/len(tup)
def deviation(reals):
    from math import sqrt
    mean = avg(reals)
    return round(sqrt(sum((i - mean)**2 for i in reals)/len(reals)),2)



ELEVATOR_SPEED = 2

def operate_elevator(t1, t2):
    e_info = ([1,0,1],[2,0,1])
    def do(instructions):
        e,*levels = instructions
        for l in levels:
            curr_lvl = e_info[e-1][2]
            # curr_time_taken = e_info[e-1][1]
            e_info[e-1][1] += abs((l - curr_lvl)*2)
            e_info[e-1][2] = l
    do(t1)
    do(t2)
    return tuple(tuple(i) for i in e_info)

def pascal(n):
    if n==1: return ((1,),)
    below = pascal(n-1)
    previous_last_row = below[-1]
    return below + ((1,) + tuple(previous_last_row[i]+previous_last_row[i+1] for i in range(n-2)) + (1,),)
