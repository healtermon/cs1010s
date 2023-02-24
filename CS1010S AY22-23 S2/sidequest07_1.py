from lazy_susan import *


def solve_trivial(t): flip_coins(t,move=tuple(True if i else False for i in get_table_state(t)))

solve_trivial_2 = solve_trivial
t2_1 = create_table(2)
run(t2_1, solve_trivial_2)

solve_trivial_4 = solve_trivial
t2_2 = create_table(4)
run(t2_2, solve_trivial_4)

t2_3 = create_table(2)
def solve_2(t):
    if check_solved(t): return
    flip_coins(t,move=(True,False))
    
run(t2_3, solve_2)

t2_4 = create_table(4)
def solve_4(t):
    moveset = [[1,0,1,0],
               [1,1,0,0],
               [1,0,0,0]]
    for move in (moveset[i] for i in (0,1,0,2,0,1,0)):
        if check_solved(t): return
        flip_coins(t,move=move)
    return
    
run(t2_4,solve_4)

def create_table_pow_2(e): return create_table(2**e)

def pow_2_moveset(e):
    if e<1: return []
    if e==1: return [[1,0]]
    p = pow_2_moveset(e-1)
    return [move*2 for move in p] + [move + [0]*2**(e-1) for move in [[1]*2**(e-1)] + p]
    
# pow_2_moveset(0)
# pow_2_moveset(1)
# pow_2_moveset(2)
# pow_2_moveset(3)
# pow_2_moveset(4)
def pow_2_moves(e):
    if e<1: return ()
    highest_index = (2**e - 1) - 1

    def moves(n):
        if n==0: return (0,)
        subcase = moves(n-1)
        return  subcase + (n,) + subcase

    return moves(highest_index)

def solve_pow_2(e):
    def solve(table):
        moveset = pow_2_moveset(e)
        for move in (moveset[i] for i in pow_2_moves(e)):
            if check_solved(table): return
            flip_coins(table,move=move)
        return
    return solve


solve_2_new = solve_pow_2(1)
t1 = create_table_pow_2(1)
run(t1,solve_2_new)

solve_4_new = solve_pow_2(2)
t2 = create_table_pow_2(2)
run(t2,solve_4_new)

solve_8_new = solve_pow_2(3)
t3 = create_table_pow_2(3)
run(t3,solve_8_new)


def get_2_pow(i):
    if i == 1: return 0
    return 1 + get_2_pow(i//2)

def solve(table):
    solve_pow_2(get_2_pow(get_table_size(table)))(table)
    return

