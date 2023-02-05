def level_up(tup):
    if len(tup)<3:
        return tup
    else:
        return (tup[0],tup[1:-1] ,tup[-1])

#print(level_up((1,2,3,4,5,6)))


def winnings(seq):
    count = 0
    for num in seq:
        count += num
        if count < 0:
            return 0
    return count


print(winnings((3,-1,2,-7,5)))
print(winnings((3,-1,2,0,5)))


def max_winnings(seq):
    tup = ()
    count = 0
    for num in seq:
        count += num
        tup += (count,)
        if count < 0:
            break
    return max(tup)

print(max_winnings((3,-1,2,-7,5)))
print(max_winnings((3,-1,2,0,5)))



def max_num():
    count = 0
    boxes = 0
    while count >=0:
        count += next_box()
        boxes += 1
    return boxes


def foo(m,n):
    if m==n:
        return m
    elif m>n:
        return foo(m-n,n)
    else:
        return foo(m,n-m)

    




    












