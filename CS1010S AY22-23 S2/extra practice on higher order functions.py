def decimal_to_binary(n):
    if n<=1: return str(n)
    return decimal_to_binary(n//2) + str(n%2)



def make_decimal_to_n_ary_converter(n):
    def to_str(x):
        if x<=9:
            return str(x)
        elif x <= 9 + 1+ord("Z")-ord("A"):
            print("reached elif")
            return chr(x-10 + ord("A"))
        else: raise Exception("wtf number did you put in? what base is this?")
    # return a number converter that takes a decimal number and returns its string representation in base n
    def decimal_to_n_ary(x):
        if x<=n-1: return to_str(x)
        print(f"at x={x}, n={n}")
        print(f"x//n={x//n},x%n={x%n}")
        return decimal_to_n_ary(x//n) + to_str(x%n)
    return decimal_to_n_ary


decimal_to_binary = make_decimal_to_n_ary_converter(2)
decimal_to_octal = make_decimal_to_n_ary_converter(8)
decimal_to_hexadecimal = make_decimal_to_n_ary_converter(16)


def hexadecimal_to_decimal(hex_number):
    # return the decimal number that hex_number represents
    return int(hex_number,16)

def make_n_ary_to_decimal_converter(n):
    # return a number converter that takes a string representation of a base n number and returns its decimal equivalent
    return lambda x: int(x,n)

def compose(f, g):
    return lambda x: f(g(x))

def make_p_ary_to_q_ary_converter(p, q):
    # return a number converter that takes a string representation of a number in base p and returns the string representation of that number in base q
    return compose(make_decimal_to_n_ary_converter(q),make_n_ary_to_decimal_converter(p))

binary_to_octal = make_p_ary_to_q_ary_converter(2, 8)
hexadecimal_to_binary = make_p_ary_to_q_ary_converter(16, 2)
octal_to_hexadecimal = make_p_ary_to_q_ary_converter(8, 16)
octal_to_binary = make_p_ary_to_q_ary_converter(8, 2)

    

