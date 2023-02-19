import copy
def copy_tree(tree):
    if type(tree) is tuple: return tuple(copy_tree(i) for i in tree)
    if type(tree) is list : return      [copy_tree(i) for i in tree]
    return copy.copy(tree)
    

# Do not remove this line
original = (1, 2, 3, 4)
