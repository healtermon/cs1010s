def dec_to_base(b, n): # Time: O(log^2 n), Space: O(log n) 
    if n<b:
        return str(n)
    else:
        return dec_to_base(b,n//b)+str(n%b)

def dec_to_base(b, n): # Time: O(log^2 n), Space: O(log n)
    result = ""
    while n>=b:
        result = str(n%b) + result
        n=n//b
    return str(n)+result

print(dec_to_base(4,0)) # "0"
print(dec_to_base(4,4)) # "10"
print(dec_to_base(4,99)) # "1203"

def base_to_dec(b,s): #Time: O(n^2), Space: O(n), where n is len(s)
    if s=="":
        return 0
    else:
        return  base_to_dec(b,s[:-1])*b+int(s[-1])

def base_to_dec(b,s): #Time: O(n^2), Space: O(n), where n is len(s)
    if s=="":
        return 0
    else:
        return  int(s[0])*(b**(len(s)-1)) + base_to_dec(b,s[1:])

def base_to_dec(b,s): #Time: O(n), Space: O(1), where n is len(s)
    result = 0
    for i in range(len(s)):
        result += int(s[i])*(b**(len(s)-i-1))
    return result

def base_to_dec(b,s): #Time: O(n), Space: O(1), where n is len(s)
    result = 0
    for i in range(len(s)):
        result += int(s[-i-1])*(b**i)
    return result

def base_to_dec(b,s): #Time: O(n), Space: O(1), where n is len(s)
    result = 0
    for i in range(len(s)):
        result *= b
        result += int(s[i])
    return result

def base_to_dec(b,s): #Time: O(n), Space: O(1), where n is len(s)
    result = 0
    for c in s:
        result *= b
        result += int(c)
    return result

def base_to_dec(b,s): #Time: O(n), Space: O(1), where n is len(s)
    result = 0
    counter = 1
    for c in s:
        result += int(c)*(b**(len(s)-counter))
        counter += 1
    return result


def base_to_dec(b,s): #Time: O(n^2), Space: O(n), where n is len(s)
    result = 0
    while s:
        result *= b
        result += int(s[0])
        s = s[1:]
    return result

print(base_to_dec(4,"1203")) # 99
print(base_to_dec(4,"10"))   # 4
print(base_to_dec(4,"0"))    # 0


def num_straights(n): #Time: O(n), Space: O(n)
    if n==1:
        return 0
    else:
        return num_straights(n-1)+ 2*n - 3
 
print(num_straights(2)) # 1
print(num_straights(5)) #16

def num_straights(n): #Time: O(n), Space: O(1)
    result = 0
    for i in range(2,n+1):
        result += 2*i-3
    return result

def gen_seq(n):
    if n==2:
        return ("F","T","F","T","F","F")
    else:
        return gen_seq(n-1) +("T",)+("F",)*(n-1)+("T",)+("F",)*n

def gen_seq(n):
    result = ("F","T","F","T","F","F")
    for i in range(3,n+1):
        result += ("T",)+("F",)*(i-1)+("T",)+("F",)*i
    return result









