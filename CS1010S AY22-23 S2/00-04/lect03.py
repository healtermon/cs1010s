# Recursive factorial
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Recursive Fibonacci
def fib(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

# Mutual recursion
def ping(n):
    if (n == 0): 
        return n
    else: 
        print("Ping!")
        pong(n - 1)
def pong(n):
    if (n == 0): 
        return n
    else: 
        print("Pong!")
        ping(n - 1)

# Iterative factorial
def factorial(n):
    product = 1
    for counter in range(2, n + 1):
        product = product * counter
    return product

# Iterative factorial, another way
def factorial(n):
    product, counter = 1, 1
    while counter <= n:
        product = product * counter
        counter = counter + 1
    return product

# range
for i in range(10):
    print(i)
for i in range(3, 10):
    print(i)
for i in range(3, 10, 4):
    print(i)

# break
for j in range(10):
    print(j)
    if j == 3:
        break
print("done")

# continue
for j in range(10):
    if j % 2 == 0:
        continue
    print(j)
print("done")

# Greatest Common Divisor
def gcd(a, b):
    if (b == 0):
        return a
    else:
        return gcd(b, a % b)

# Tower of Hanoi
def move_tower(size, src, dest, aux):
    if size == 0:
        return True
    else:
        move_tower(size-1, src, aux, dest)
        print_move(src, dest)
        move_tower(size-1, aux, dest, src)
def print_move(src, dest):
    print("move top disk from ", src," to ", dest)

# Exponentiation
def power(b, e):
    if e == 0:
        return 1
    else:
        return b * power(e - 1)

# Fast exponentiation
def fast_expt(b, e):
    if e == 0:
        return 1
    elif e % 2 == 0:
        return fast_expt(b*b, e/2)
    else:
        return b * fast_expt(b, e-1)