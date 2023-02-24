def at_least_n(lst, n):
    for i in range(len(lst)):
        if lst[i] < n:
            lst.remove(lst[i])
    return lst
def at_least_n(lst, n):
    for i in lst:
        if i < n:
            lst.remove(i)
    return lst

# from https://rednafi.github.io/reflections/modify-iterables-while-iterating-in-python.html
l = [3, 4, 56, 7, 10, 9, 6, 5]

for i in l:
    print(i)
    if i % 2 == 0:
        l.remove(i)

print(l)


# 1c
def at_least_n(lst, n):
    for i in reversed(lst):
        if i<n: lst.remove(i)
    return lst

def at_least_n(lst, n):
    return [i for i in lst if i>=n]


### DO NOT MODIFY THIS ###
lst1 = list(range(10))  
lst2 = list(range(8))
lst3 = list(range(6,10))

def transpose_new(m):
    return [[row[c] for row in m] for c in range(len(m[0]))]

def transpose(m):
    m_new = transpose_new(m)
    m.clear()
    m.extend(m_new)
    return m
    

### DO NOT MODIFY THIS ###
matrix1 = [[ 1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
matrix2 = [[ 1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
matrix3 = [[1, 2, 3]]
matrix4 = [[1, 2],
           [4, 5],
           [7, 8]]

def row_sum(m):
    return [sum(row) for row in m]

def col_sum(m):
    return [sum(row[c] for row in m) for c in range(len(m[0])) ]
[1, [2, 1], 1, [3, [1, 3]], [4, [1], 5], [1], 1, [[1]]].count(1)

def pop_at_index(seq, index):
    l = len(seq)
    if index not in range(-l,l): return seq
    return seq[:index] if index==-1 else seq[:index] + seq[index+1:]

def insertionsort_ascending_new_list_recursive(l:list,key=lambda x:x):
    def sort(x:list,y:list):
        if y == []: return x
        for i,e in enumerate(x):
            if key(y[0]) < key(e):
                x.insert(i,y.pop(0))
                return sort(x,y)
        x.append(y.pop(0))
        return sort(x,y)
    return sort([],l)
    
def selectionsort_ascending_inplace(l:list,key=lambda x:x):
    endi = len(l)
    for i in range(0,endi-1):
        mini = i
        # print("i",i)
        for j in range(i+1,endi):
            if key(l[j]) < key(l[mini]):
                # print(j,"smaller than",mini)
                mini = j
        # print("mini",mini,"i",i)
        l[i],l[mini] = l[mini],l[i]
        print(l)
    return l
            
def bubblesort_ascending_inplace(l:list,key=lambda x:x):
    endi = len(l)-1
    for i in range(0,endi):
        for j in reversed(range(i,endi)):
            if key(l[j]) > key(l[j+1]): l[j],l[j+1] = l[j+1],l[j]
    return l

# I ALWAYS FORGET TO RETURN THE LIST ITSELF AFTER WRITING THE SEARCH, ARGHHHH

# the only sort that was correct on first try
def mergesort_ascending_new_list(l:list,key=lambda x:x):
    n = len(l)
    if n<=1: return l
    avgi = n//2
    l1 = mergesort_ascending_new_list(l[:avgi])
    l2 = mergesort_ascending_new_list(l[avgi:])
    new_l = []

    while(l1 and l2):
        new_l.append(l1.pop(0) if key(l1[0]) < key(l2[0]) else l2.pop(0))
    new_l.extend(l1)
    new_l.extend(l2)
    return new_l
        

# Insertion Sort
[5, 7, 4, 9, 8, 5, 6, 3]
[3, 5, 7, 4, 9, 8, 5, 6]
[3, 4, 5, 7, 9, 8, 5, 6]
[3, 4, 5, 7, 8, 9, 5, 6]
[3, 4, 5, 5, 7, 8, 9, 6]
[3, 4, 5, 5, 6, 7, 8, 9]

# Selection  Sort
[5, 7, 4, 9, 8, 5, 6, 3]
[3, 7, 4, 9, 8, 5, 6, 5]
[3, 4, 5, 9, 8, 7, 6, 5]
[3, 4, 5, 5, 8, 7, 6, 9]
[3, 4, 5, 5, 6, 7, 8, 9]


# Bubble Sort, my favourite 'cuz it's the simplest
[5, 7, 4, 9, 8, 5, 6, 3]
[5, 7, 4, 9, 8, 5, 3, 6]
[5, 7, 4, 9, 8, 3, 5, 6]
[5, 7, 4, 9, 3, 8, 5, 6]
[5, 7, 4, 3, 9, 8, 5, 6]
[5, 7, 3, 4, 9, 8, 5, 6]
[5, 3, 7, 4, 9, 8, 5, 6]
[3, 5, 7, 4, 9, 8, 5, 6]
[3, 5, 7, 4, 9, 5, 8, 6]
[3, 5, 7, 4, 5, 9, 8, 6]
[3, 5, 4, 7, 5, 9, 8, 6]
[3, 4, 5, 7, 5, 9, 8, 6]
[3, 4, 5, 7, 5, 9, 6, 8]
[3, 4, 5, 7, 5, 6, 9, 8]
[3, 4, 5, 5, 7, 6, 9, 8]
[3, 4, 5, 5, 7, 6, 8, 9]
[3, 4, 5, 5, 6, 7, 8, 9]

# Quick Sort
[5, 7, 4, 9, 8, 5, 6, 3]
[5, 7, 4, 9,]   [ 8, 5, 6, 3]
[5, 7][ 4, 9]   [ 8, 5][ 6, 3]
()[5][ 7]   ()[4][ 9]   ()[ 8][ 5]   ()[ 6][ 3]
(5)[][ 7]   (4)[][ 9]   (5)[ 8][]   (3)[ 6][]
(5,7)[][]   (4,9)[][]   (5,8)[][]   (3,6)[][]
(5,7)[][]   (4,9)[][]   (5,8)[][]   (3,6)[][]
()[5, 7][4, 9]      ()[5,8][3,6]
(4)[5, 7][9]      (3)[5,8][6]
(4,5)[7][9]      (3,5)[8][6]
(4,5,7)[][9]      (3,5,6)[8][]
(4,5,7,9)[][]      (3,5,6,8)[][]
()[4,5,7,9][3,5,6,8]
(3)[4,5,7,9][5,6,8]
(3,4)[5,7,9][5,6,8]
(3,4,5)[7,9][5,6,8]
(3,4,5,5)[7,9][6,8]
(3,4,5,6)[7,9][8]
(3,4,5,6,7)[9][8]
(3,4,5,6,7,8)[9][]
(3,4,5,6,7,8,9)[][]
[3,4,5,6,7,8,9]
