# 1. a way of marking where it has travelled before so it can complete a loop
# 2. creating new paths, one per list item
# 3. a way of comparing loops and seeing which one is equal to another so we can filter
# 4. a way of checking whether something is a list or not "type(x) is list"
# 5. fundamentally it's an iterative algorithm because to know when to stop it needs to store where it has been. What it will do will depend on where it has been. TODO: I don't know how to do wishful thinking on this.
# 6. a way to differentiate between links to the same item in a list, from different indexes
def pp(x): [print(i) for i in x]

def get_cycles(x, path=None) -> list:
    """returns a list of cycles like [a,b,a], and it takes the next item and a list of where it has been.
    firstly, check whether thing given is a list. If it's not, just return an empty list representing no solutions.
    upon entering a list it will
    index the items in the list (for 6), for each item that is not a list(which are the only "link"s here):
    - if the item is the same as any in the path, it has completed 1 loop. Cool! add the index then the item to the path, trim the path to the cycle alone and add that as a solution
    - if the item is new, add the index then the item to the path, then call getcycles with this new path on the list and add the solutions gotten back to the list of solutions
    """
    def trim_to_cycle_alone(l:list) -> list:
        """assumes the last item is where the cycle starts, trims everything before the first occurance of that in the list.
        Does not account for any lists that don't have 2 references to the exact same list in it."""
        for i in range(len(l)):
            if l[i] is l[-1]: return l[i:]
            # not even gonna return anything, just throw exception
        raise Exception("Sorry, list does not contain cycle") 

    def is_in_path(x,path):
        for item in path:
            if x is item: return True
        return False
    
    if type(x) is not list: return []
    if path is None: path = [x]  # for (3), noting down the first list you enter
    print(f"Entering NEW LIST:{x}")
    sols = []
    for i,item in enumerate(x):
        if type(item) is not list: continue # this line is not needed as get_cycles checks whether x[i] is a list in the first line, but makes reasoning about the code simpler as you only consider lists(links) in your thinking. It can be regarded as an optimisation, not needing to create a whole new list.
        unique_path = path + [i,item] # appending the index of the item is for (6), appending the list itself is needed for (3)
        print(f"Unique_path:{unique_path}")
        if is_in_path(item,path): # "if e in path" gets "RecursionError: maximum recursion depth exceeded in comparison" so I use a less ambiguous way to do it
            sols += [trim_to_cycle_alone(unique_path)] 
        else:
            sols += get_cycles(item,unique_path)
    return sols

def remove_duplicates_from_list(l:list,comparison_operator) -> list:
    """comparison operator should take 2 arguments. Compares the first thing in the list to every other,
    and if it matches, creates another list with the first thing removed, then calls itself on the rest of the list.
    Otherwise the item has no duplicates, and concatenates the first item to the result of calling itself on the rest of the list instead.
    This is lisp-style function, unfortunately not as fast due to the different implementation of lists, but simple enough to be easy to implement and read"""
    if len(l)<=1: return l
    first,rest = l[0],l[1:]
    for i in rest:
        if comparison_operator(first,i): return remove_duplicates_from_list(rest,comparison_operator)
    return [first] + remove_duplicates_from_list(rest,comparison_operator)
    
def remove_duplicate_cycles(l:list) -> list:
    """takes a list of cycles, removes duplicates by checking each list against every other"""
    def equal_paths(p1:list,p2:list) -> bool: # TODO: test whether this works, honestly it looks simple enough that it should work
        """because I don't trust python's built-in '==' operator"""
        def equal_path_item(x,y) -> bool:
            if type(x) is not type(y): return False
            if type(x) is list: return x is y
            elif type(x) is int: return x == y
            else: raise Exception("where the fuck are you using this function? The things u compare are neither integers or lists")
        
        if len(p1) != len(p2): return False
        for i in range(len(p1)):
            if not equal_path_item(p1[i],p2[i]): return False
        return True
    return remove_duplicates_from_list(l,equal_paths)

def count_cycles(x) -> int:
    a = get_cycles(x)
    b = remove_duplicate_cycles(a)
    c = len(b)
    print("cycles gotten:")
    pp(a)
    print("after removing duplicates")
    print(b)
    return c
    # return len(remove_duplicate_cycles(get_cycles(x)))
    

a = [1,2]
a1 = [2,a]
a[1] = a1
# ^count 1
b = [1,None]
c = [b,b]
b[0] = b
# count 1
d = [1,2]
e = [d,d]
d[0],d[1] = e,e
# count 4
f = [1,2]
g = [1,2]
g[0],g[1] = f,g
f[0],f[1] = g,f
# count 3


t1 = [(1,), (1,)]
count_cycles(t1)# 0

t2 = [ (1,), [ (2,), (0,)]]
count_cycles(t2)# 0

t3 = [ (1,), [ (2,), (0,)]]
t3[1][1] = t3
count_cycles(t3)# 1

helper = [(),()]
helper[1] = helper
t4 = [helper, helper]
count_cycles(t4)# 1

helper2 = [(),()]
t5 = [helper2, helper2]
helper2[0] = t5
helper2[1] = t5
count_cycles(t5) # 4

t6 = [ (True,), (True,)]
helper3 = [(True,), (True,)]
t6[0] = helper3
t6[1] = t6
helper3[0] = t6
helper3[1] = helper3
count_cycles(t6) #3
