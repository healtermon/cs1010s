# tricky question, an integer approach won't work as the leading zeros will be
# destroyed when passing to the function, leaving no other choice but to use
# strings. I don't know how to write one that generates a recursive process.
def replace_digit(n, d, r):
    str(n).replace(str(d))

def replace_digit_iterative(n,d,r):
    return "".join([str(r) if c==str(d) else str(c)
                    for c in str(n)])
