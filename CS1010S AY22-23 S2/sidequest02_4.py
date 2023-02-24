###########
# Task 1a #
###########

### Simplifed Order Notations

# 4**n * n**2      # Ans: O(4**n * n**2)
# n * 3**n         # Ans: O(n * 3**n)
# 1000000000n**2   # Ans: O(n**2)
# 2**n/1000000000  # Ans: O(2**n)
# n**n + n**2 + 1  # Ans: O(n**n)
# 4**n + 2**n      # Ans: O(4**n)
# 1**n             # Ans: O(1)
# n**1             # Ans: O(n)
# (n + 3)**4       # Ans: O(n**4)
# (n + 4)**3       # Ans: O(n**3)
# e**n + n**2      # Ans: O(e**n)
# n**7 + 3**n      # Ans: O(3**n)

# Leave this commented line here!

###########
# Task 1b #
###########

### Larger order-of-growth in each group

# i.   (4**n * n**2) vs (n * 3**n)
# Ans: O(4**n * n**2)

# ii.  (1000000000*n**2) vs (2**n/1000000000)
# Ans: O(2**n)

# iii. (n**n + n**2 + 1) vs (4**n + 2**n)
# Ans: O(n**n)

# iv.  (n + 3)**2 vs (n + 2)**3
# Ans: O(n**3)

# v.  (e**n + n**2) vs (n**7 + 2**n)
# Ans: O(e**n)

# vi.  (1**n + 2**n + 3**n) vs (n**3 + n**2 + n**1)
# Ans: O(3**n)

# Leave this commented line here!


###########
# Task 1c #
###########

### Arranging order of growths in ascending order

# 1:  O(1)          
# 2:  O(n)          
# 3:  O(n**2)       
# 4:  O(n**3)       
# 5:  O(n**4)       
# 6:  O(2**n)       
# 7:  O(e**n)       
# 8:  O(3**n)       
# 9:  O(n * 3**n)   
# 10: O(4**n)       
# 11: O(4**n * n**2)
# 12: O(n**n)       

# Leave this commented line here!

# task 2
def foo(n):
    def bar(n):
        if n == 0:
            return 0
        else:
            return 1 + bar(n-1)
    def alt_bar(n): return n
    return n*bar(n)

def alt_foo(n): return n*n

# time complexity: O(n)
# space complexity: O(n)

# task 3
def bar(n):
    """sum of natural numbers from 0 to n, time complexity O(n), space complexity O(n)"""
    if n == 0:
        return 0
    else:
        return n + bar(n-1)
def alt_bar(n): return (n * (n+1))//2

def foo(n):
    """time complexity O(n^2), space complexity O(n)"""
    if n == 0:
        return 0
    else:
        return bar(n) + foo(n-1)
    
# time and space complexity O(1)
def improved_foo(n): return (n*(n+1)*(n+2))//6

