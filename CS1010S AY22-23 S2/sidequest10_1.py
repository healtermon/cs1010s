# pain-in-the-ass sidequest, never doing it again! so many hours of debugging, and no template file so no viewing the fruits of your labor...
from puzzle import *
from random import randrange
from mission03 import reduce,repeated,compose

def flatten(l:list) -> list:
    if type(l) is not list: return [l]
    if len(l) == 0: return l
    for i in l: return flatten(l[0]) + flatten(l[1:])

def new_game_matrix(n): return [[0]*n for i in range(n)]
def has_zero(mat): return 0 in flatten(mat) 
def add_two(mat):
    """randomly tries inserting everywhere. If successful, exit. Will optimise for speed if it's the bottleneck."""
    if not has_zero(mat): return mat
    n = len(mat)
    while True:                
        x1 = randrange(n)       # I use randrange instead of randint 'cuz it randint calls randrange and it makes the code clearer
        x2 = randrange(n)
        # once a number is added, get out
        if mat[x1][x2] == 0:
            mat[x1][x2] = 2
            break
    return mat

# task 2
def has_same_adjacent_tiles(mat):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            # print(f"x1={x1},x2={x2},{x1+1 in range(n)}, {x2+1 in range(n)}")
            # only checks to the right and below, to reduce redundant operations
            if i+1 in range(n) and mat[i][j] == mat[i+1][j]: return True
            if j+1 in range(n) and mat[i][j] == mat[i][j+1]: return True
    return False
                
def game_status(mat):
    if [i for i in flatten(mat) if i>=2048]: return "win"
    if not has_zero(mat) and not has_same_adjacent_tiles(mat): return "not over"
    return "lose"

# task 3a
def transpose(mat):
    """assumes matrices are mxn sized and made of lists of lists, not some weird irregular-sized list like [[1,2],[1],[1,2,3]]"""
    m = len(mat)
    n = len(mat[0])
    return [[mat[i][j] for i in range(m)] for j in range(n)]

# task 3b
def reverse(mat):
    return [i[::-1] for i in mat]
# task 3c
def pad_value(val,n,l): return l + [val]*(n - len(l))
def pad_zeros(n,l): return pad_value(0,n,l)
        
def merge_row_left(l):
    n = len(l)
    no_zeros = (i for i in l if i!=0)
    score = 0
    lefted = []
    curr_tile = next(no_zeros,None)
    next_tile = next(no_zeros,None)
    while curr_tile is not None:
        if curr_tile == next_tile:
            lefted.append(curr_tile+next_tile)
            score += curr_tile+next_tile
            curr_tile = next(no_zeros,None)
            next_tile = next(no_zeros,None)
        else:
            lefted.append(curr_tile)
            curr_tile = next_tile
            next_tile = next(no_zeros,None)
    return (pad_zeros(n, lefted),score)
    
    
def merge_left(mat):
    # print(mat)
    rows,scores = zip(*map(lambda row: merge_row_left(row), mat))
    new_mat = list(rows)
    return (new_mat,new_mat!=mat, sum(scores))
def merge_dir(mat,fs):
    new_matrix, is_valid, score_increment = merge_left(compose(*fs[::-1])(mat))
    return (compose(*fs)(new_matrix), is_valid, score_increment)
def merge_right(mat): return merge_dir(mat, [reverse])
def merge_up(mat): return merge_dir(mat,[transpose])
def merge_down(mat): return merge_dir(mat,[transpose,reverse])
    

# task 4
def make_state(mat,score): return (mat,score)
def make_new_game(n): return make_state(repeated(add_two,2)(new_game_matrix(n)),0)
def get_score(state): return state[1]
def get_matrix(state): return state[0]
def direction(state,merge_d):
    new_matrix, is_valid, score_increment = merge_d(get_matrix(state))
    return (make_state(add_two(new_matrix) if is_valid else new_matrix,
                       get_score(state)+score_increment),
            is_valid)
def up(state): return direction(state,merge_up)
def down(state): return direction(state,merge_down)
def left(state): return direction(state,merge_left)
def right(state): return direction(state,merge_right)

# task 5

def make_new_record(mat, increment): return (mat,increment)
def get_record_matrix(record): return record[0]
def get_record_increment(record): return record[1]

def make_new_records(): return []
def is_empty(stack_of_records): return stack_of_records==[]
def push_record(new_record,stack_of_records): stack_of_records.append(new_record)
def pop_record(stack_of_records):
    # This makes no sense, the return should be (record,stack_of_records) so it doesn't break abstract data structure layer
    if is_empty(stack_of_records): return (None, None, stack_of_records)

    last_record = stack_of_records.pop()
    return (get_record_matrix(last_record), get_record_increment(last_record), stack_of_records)

def make_state(mat,score,record_stack,consecutive_undos): return (mat,score,record_stack,consecutive_undos)
def make_new_game(n): return make_state(repeated(add_two,2)(new_game_matrix(n)),0, make_new_records(),0)
def get_records(state): return state[2]
def get_consecutive_undos(state): return state[3]
def direction(state,merge_d):
    new_matrix, is_valid, score_increment = merge_d(get_matrix(state))
    if is_valid:
        push_record(make_new_record(get_matrix(state),score_increment),get_records(state))
        new_state = make_state(add_two(new_matrix), get_score(state) + score_increment, get_records(state), 0)
    else:
        new_state = make_state(new_matrix, get_score(state), get_records(state), get_consecutive_undos(state))
    return (new_state, is_valid)

def undo(state):
    record_stack = get_records(state)
    if get_consecutive_undos(state)==3 or is_empty(record_stack): return (state,False)
    last_matrix,last_score_increment,updated_stack = pop_record(record_stack)
    return (make_state(last_matrix,
                       get_score(state)-last_score_increment,
                       updated_stack,
                       get_consecutive_undos(state)+1),
            True)
    
    
