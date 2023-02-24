def remove_extras(nums:tuple):
    def remove_extras_from_start(tup:tuple):
        # if len(tup) <= 1: return tup
        if tup == (): return ()
        fst = tup[0]
        rst = tup[1:]
        if fst in rst: return remove_extras_from_start(rst)
        else: return (fst,) + remove_extras_from_start(rst)
   
    if type(nums) is not tuple: raise Exception("wtf not a tuple, what are u passing it?")
    return remove_extras_from_start(nums[::-1])[::-1]

# "DOES NOT WORK because it fucks up order"
# def remove_extras_via_set(nums):
#     return tuple(set(nums))

def reverse_iterative_splicing(x:str):
    return x[::-1]

def reverse_recursion(x:str):
    if len(x)<=1: return x
    return reverse_recursion(x[1:]) + x[0]


def reverse_iterative(x:str):
    result = ""
    while(x):
        b4_lst = x[:-1]
        lst = x[-1]
        
        result = result + lst
        x = b4_lst
    return result

# without converting to string, an iterative solution
def highest_place(y:int):
    if abs(y) < 10: return 0
    return 1 + highest_place(y//10)
def highest_place_iterative_wrong1(y:int):
    hi = 0
    while(abs(y)):
        y//=10
        hi+=1
    return hi-1
def highest_place_iterative(y:int):
    hi = 0
    while(abs(y)>9):
        y//=10
        hi+=1
    return hi

def reverse_number(x:int):
    # negative = x<0
    # x = abs(x)
    pow = highest_place(x)
    res = 0
    while(x):
        print("res=",res)
        res += (x%10)*10**pow
        pow -= 1
        x //= 10
    return res

def reverse_number_recursive(x:int): # guess it's recursive after all
    # negative = x<0
    # x = abs(x)
    res = 0
    while(x):
        print("res=",res)
        res += x%10 * 10**highest_place(x)
        x //= 10
    return res
def reverse_number_ref_sol(num):
    reversed_num = 0
    while num != 0 :
        curr_digit = num % 10
        reversed_num = 10*reversed_num
        reversed_num = reversed_num + curr_digit
        num = num // 10
    return reversed_num
