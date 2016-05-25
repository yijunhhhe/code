# Define function
def my_abs(x):
    if x>= 0:
        return x
    else:
        return -x

# if the function is empty
def nop():
    pass
#or
    if age >= 18:
        pass

# Parameter check
def my_abs(x):
    if not isintance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# Return different value
from math import cos, sin
import math

def move(x, y, step, angle = 0):
    nx = x + step * cos(angle)
    ny = y - step * sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi/6)
print(x,y)

a = 4+12/7-1 * 2
b = 4+12/(7-1) *2
print(a, b)