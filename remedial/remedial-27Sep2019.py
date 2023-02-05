def house_visit(block,house_num,h): # Time: O(h), Space: O(h)
    if h==0:
        return 0
    else:
        return block[house_num] + house_visit(block,house_num+1,h-1)

def house_visit(block,house_num,h): # Time: O(h), Space: O(1)
    result = 0
    for i in range(h):
        result += block[house_num+i]
    return result

def house_visit(block,house_num,h): # Time: O(h), Space: O(1)
    result = 0
    for i in range(house_num,house_num+h):
        result += block[i]
    return result

# n is the number of houses
def good_visit(block,h): # Time: O(nh), Space: O(1)
    score = house_visit(block,0,h)
    n = len(block)
    for i range(n-h):
        new_score = house_visit(block,i+1,h)
        if new_score > score:
            score = new_score
    return score

def fold(op, f, n):
    if n == 0:
        return f(0)
    else:
        return op(f(n), fold(op, f, n-1))

def good_visit(block, h):
    def f(n):
        return house_visit(block,n,h)
    def op(x,y):
        return max(x,y)
    return fold(op, f, len(block)-h+1)

def good_visit(block,h): # Time: O(n^2), Space: O(n^2)
    if h>len(block):
        return 0
    else:
        score = house_visit(block,0,h)
        rest_score = good_visit(block[1:],h)
        if score > rest_score:
            return score
        else:
            return rest_score

def best_visit(block):
    score = 0
    for i in range(len(block)):
        score = max(score,good_visit(block,i))
    return score

# Order of growth
# goood_visit => Time: O(nh), Space: O(1)
# Time: O(n^2h), Space: O(1)

# goood_visit => Time: O(n^2), Space: O(n^2)
# Time: O(n^3), Space: O(n^2)


def best_with_first(block): # Time: O(n^2), Space: O(n)
    result = block[0]
    for i in range(len(block)):
        result = max(result,sum(block[:i]))
    return result

def best_visit(block): # Time: O(n^3), Space: O(n^2)
    if block == ():
        return 0
    else:
        return max(best_with_first(block), best_visit(block[1:]))
    













