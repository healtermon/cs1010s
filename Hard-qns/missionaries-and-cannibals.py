# missionaries = m, cannibals = c
# places are src,end,boat.
# find any minimal step pattern of (c,m) showing no. of ppl on boat, starting from src to end, in a tuple like ((c1,m1),(c2,m2),(c3,m3)).
# If the beginning state is invalid, return False.
# condition 1: boat must hold 1 or 2 ppl, 1 just to row the boat
# condition 3: c <= m at every place
# cannibal(1,2):
# (1,1), 0,1 1,1 (1,0), 1,1 0,1
# (1,1)  0,0 1,2
# cannibal(2,2):
# (2,0), 0,2 2,0 (1,0), 1,2 1,0
# (0,2), 1,0 1,2 (1,0), 2,0 0,2
# (2,0)  0,0 2,2
# cannibal(3,3):
# (2,0), 1,3 2,0 (1,0), 2,3 1,0
# (2,0), 0,3 3,0 (1,0), 1,3 2,0
# (0,2), 1,1 2,2 (1,1), 2,2 1,1
# (0,2), 2,0 1,3 (1,0), 3,0 0,3
# (2,0), 1,0 2,3 (1,0), 2,0 1,3
# (2,0)  0,0 3,3
# cases: (2k 2nk)->(2k 2k) (3k 3nk)->(3k 3k) (4k 4nk)->(2k 2nk)
# cannibal(2k,2k):
# (2 0) 0k 2k 2k 0k (1 0)
# OPTIMISATIONS
# - 5 possible choices: (0,1)(1,0)(0,2)(2,0)(1,1)
# - most efficient list would never bring ppl back from end to src; every 2 trips will bring one person from src to end
# -
# NAMING
# time_place (state), where
# - time in {init cur(rent, I use nothing to represent this) fin}
# - place in {src des(tination)}
# step/steps 
def pp(x): [print(i) for i in x]
C = 0                       # constants to access tuple
M = 1
def cond3(place): return place[C] <= place[M]

def is_even(x): return not x%2
def des(steps):
    return is_valid_through()
def is_valid_thorough(init_src,steps,pred):
    (des_c,des_m) = init_src
    for i in range(len(steps)):
        if is_even(i):
            des_c += steps[i][C]
            des_m += steps[i][M]
        else:
            des_c -= steps[i][C]
            des_m -= steps[i][M]

        if not pred((des_c,des_m) or not pred(())): return False
        
    return (des_c,des_m)
    
def score(steps):
    l = len(steps)
    if l%2: l-=1                # trim to make even
    d = des(steps[:l])
    return d[C] + d[M]

def cannibal(c,m):
    pass
