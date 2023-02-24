a = [6, 4, 2, 9, 10, 4, 2, 1, 3]
def accumulate(fn, initial, seq):
    if not seq: # if seq is empty
        return initial
    else:
        return fn(seq[0], accumulate(fn, initial, seq[1:]))
# Task 1a #
def search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the first
    position that x should go to such that it will be less than or equal to
    the next element in the list. """
    if len(seq)<1: return 0
    i = 0
    for i,e in enumerate(seq):
        if x <= e: return i
    return i+1
# Task 1b #
def binary_search(x, seq):
    """ Takes in a value x and a sorted sequence seq, and returns the first
    position that x should go to such that it will be less than or equal to
    the next element in the list. Uses O(lg n) time complexity algorithm. """
    def recur(s,e):
        if s == e: return s if x < seq[s] else s+1
        
        m = (s+e)//2
        if x == seq[m]: return m
        if x <  seq[m]: return recur(s,m-1)
        else:           return recur(m+1,e)
    
    return recur(0,len(seq)-1)

# Task 2a #
def insert_list(x, lst):
    """ Inserts element x into list lst such that x is less than or equal
        to the next element and returns the resulting list."""
    lst.insert(search(x,lst),x)
    return lst

# Task 2b #
def insert_tup(x, tup):
    """ Inserts element x into tuple tup such that x is less than or equal
        to the next element and returns the resulting tuple."""
    i = search(x,tup)
    return tup[:i] + (x,) + tup[i:]

# Task 2c #
tup = (5, 4, 10)
output_tup = insert_tup(7, tup)
lst = [5, 4, 10]
output_lst = insert_list(7, lst)
print(tup is output_tup)
#=> Output:False
# this is false as every tuple is immutable, so tuples with different contents, like these 2, are never the same object in python
print(tup == output_tup)
#=> Output:False
# this is false as the tuples' contents are not the same. They are even of different lengths.
print(lst is output_lst)
#=> Output:True
# since output_lst returns the original list, both variables reference the same list object, and hence the is operator will check the same addresses, and say they are the same object reference.
print(lst == output_lst)
#=> Output:True
# Since the two variables have the same object reference binded to them, the == operator will check a list against itself, which of course, returns True.

# Task 3a #
def sort_list(lst):
    """ Sorts list lst in ascending order."""
    new_l = []
    for e in lst:               # n time complexity
        insert_list(e,new_l)    # n time complexity. insert_list is n, and calls search, which is also n, once. So together they are 2n. so 2n * n = 2n^2, which means n^2 time complexity
    return new_l

# Task 3b #
#=> Time complexity of sort_list: O(n^2) 

# Task 3c #
def sort_tup(tup):
    """ Sorts tuple tup in an ascending order."""
    return accumulate(lambda x,y:insert_tup(x,y), (), tup)

# Task 4a #
import shelf

# Please uncomment the test function calls to see the animation

def insert_animate(block_pos, shelf, high):
    """
    Pops the block at block_pos and inserts it in the position in the shelf
    such that its size is less than or equal to the one succeeding it. It searches
    for this position within zero and high.

    NOTE: To actually see the animation, please uncomment the testing function
    below.
    """
    b = shelf.pop(block_pos)
    high = high-1 if block_pos < high else high
    
    for i in range(high):     # as there is 1 less block
        if b.size <= shelf[i].size:
            shelf.insert(i,b)
            return shelf
    
    # optional to return shelf but we do this for debugging
    shelf.insert(high,b)
    return shelf

# Test cases for insert_animate

def test_insert_animate():
    shelf.clear_window()
    s = shelf.init_shelf((2, 6, 1, 4, 8, 3, 9))
    print("## Q4a ##")
    print(insert_animate(0, s, 0))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(1, s, 1))
    # => [Block size: 2, Block size: 6, Block size: 1, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(2, s, 2))
    # => [Block size: 1, Block size: 2, Block size: 6, Block size: 4, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(3, s, 3))
    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]
    print(insert_animate(6, s, 6))
    # => [Block size: 1, Block size: 2, Block size: 4, Block size: 6, Block size: 8, Block size: 3, Block size: 9]

# Uncomment function call to test insert_animate()
#test_insert_animate()

###########
# Task 4b #
###########

def sort_me_animate(shelf):
    """
    Maintains a sorted portion and inserts every block in the shelf into the
    sorted portion.

    NOTE: To actually see the animation, please uncomment the testing function
    below.

    """

    for i in range(len(shelf)): # it may not be to the power of n now, but it may be later.
        high = i
        insert_animate(i,shelf,i)

        
    # optional to return shelf but we do this for debugging
    return shelf

# Test cases for sort_me_animate

def test_sort_me_animate():
    shelf.clear_window()
    s = shelf.init_shelf((5,2,6,9,1,4,8,3))
    print("## Q4b ##")
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 3, Block size: 4, Block size: 5, Block size: 6, Block size: 8, Block size: 9]
    shelf.clear_window()
    s = shelf.init_shelf((4, 8, 2, 9, 3, 1, 2, 3, 4, 10, 7, 5, 6))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 2, Block size: 2, Block size: 3, Block size: 3, Block size: 4, Block size: 4, Block size: 5, Block size: 6, Block size: 7, Block size: 8, Block size: 9, Block size: 10]

# Test case to catch mutation while sorting

def test_sort_me_with_duplicates():
    shelf.clear_window()
    s = shelf.init_shelf((1,3,4,1,3,2))
    print(sort_me_animate(s))
    # => [Block size: 1, Block size: 1, Block size: 2, Block size: 3, Block size: 3, Block size: 4]

# Uncomment function call to test sort_me_animate()
#test_sort_me_animate()
#test_sort_me_with_duplicates()
