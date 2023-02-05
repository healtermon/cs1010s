from math import sqrt, floor
def perfect_number(number):
    if number == 1: return False
    return number == sum(i + number//i for i in range(2,floor(sqrt(number))+1) if number%i==0)+1
