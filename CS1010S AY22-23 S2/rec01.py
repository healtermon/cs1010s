| Operator | Integer | Floating point | String                   |
|----------+---------+----------------+--------------------------|
| +        |         |                |                          |
| -        |         |                | x                        |
| *        |         |                | x(when both are strings) |
| /        |         |                | x                        |
| **       |         |                | x                        |
| //       |         |                | x                        |
| %        |         |                | x                        |
| <        |         |                |                          |
| >        |         |                |                          |
| <=       |         |  |                          |
| >=       |         |                |                          |
| ==       |         | fuckign weird, look below               |                          |
| !=       |         |                |                          |

329.00000000000011112122938 == 329.00000000000091234109472397139041
False
>>> 329.00000000000011112122938 == 329.00000000000000001234109472397139041
False
>>> 329.00000000000011112122938 == 329.0000000000000000000000000000001234109472397139041
False
>>> 329.00000000000000000000000000000011112122938 == 329.0000000000000000000000000000001234109472397139041
True
>>> 329.00000000000011112122938 == 329.00000000000091234109472397139041
False
>>> 329.00000000000011112122938 == 329.00000000000000001234109472397139041
False
>>> 329.00000000000011112122938 == 329.0000000000000000000000000000001234109472397139041
False
>>> 329.00000000000000000000000000000011112122938 == 329.0000000000000000000000000000001234109472397139041
True


x = 3
y = 5
z = -2

x + y / z                       # -2.5+3 = 0.5
x**y%x                          # 3*3*3*3*3 % 3 = 0
y <= z                          # False
x > z * y                       # True
y // x                          # 1.666666
x + z != z + x                  # False
if True: 1+1                    # 2
else: 17

if False: False
else: 42                        # 42

if (x > 0): x                   # 3
else: (-x)

if 0: 1
else: 2                         # 2

if x: 7                         # 7
else: what-happened-here

if True: 1                      # 1
elif (y>1): False
else: wake-up


def biggie_size(combo): return combo+4
def unbiggie_size(combo):return combo-4
def is_biggie_size(combo):return combo>4
def combo_price(combo): return 1.17 if is_biggie_size else 0.5
def empty_order(): return 0
def add_to_order(order,combo): return int(str(order)+str(combo))
