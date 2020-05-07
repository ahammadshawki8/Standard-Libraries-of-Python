# math module
import math

# we can see all the methods of math module.
print(dir(math))

# we can see that we have different important methods here.
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh',
#  'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'comb', 'copysign', 'cos', 'cosh',
#  'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor',
#  'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 
# 'isnan', 'isqrt', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'perm',
#  'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

# calculate natural logarithm
print(math.log(10))

# calculate common logarithm
print(math.log10(100))

# calculate 2 based logarithm
print(math.log2(1024))

# calculate factorial of any number
print(math.factorial(9))

# calculate square root of any positive number
print(math.sqrt(100))

# calculate square root of any negative number.
# here the square root of any negative number is a complex number.
import cmath # we need to import cmath module which stands for complexmath
print(cmath.sqrt(-20))

# using floor method
# floor method rounds a number to its lower nearest integer.
print(math.floor(2.34))

# using ceil method
# ceil method rounds a number to its higher nearest integer.
print(math.ceil(2.34))

# print the value of pi
import math
print(math.pi)
# print the value of tau
print(math.tau)
# print the value of e
print(math.e)

# calculate the area of a circle.
def circle_area(radius):
    area=math.pi*(radius**2)
    return area
print(circle_area(10))

# using Euelers constant
print(math.e)

# convert degrees to radians
print(math.radians(180))

# convert radians to degrees
print(math.degrees(3))

# basic trigonometry
# using sin method
print(math.sin(math.pi/2))# here the arguement is given in radians.

# using cos method
print(math.cos(0))

# using tan method
print(math.tan(math.pi/4))

# using asin(arcsin) method
print(math.asin(1))# here the arguement is given in radians.
# we can convert it to degrees.
print(math.degrees(math.asin(1)))

# using acos(arccos) method
print(math.acos(1))

# using atan(arctan) method
print(math.atan(1))

# calculate gcd of numbers
print(math.gcd(120,90))

# we can use the gamma() function.
print(math.gamma(100))

# we can even find the remainder of float using the remainder() function.
print(math.remainder(100.123,3.1))

# we can even find the power of float using pow() function.
print(math.pow(2.33,4.573))
# we can do it in this way too.
print(2.33**4.573)

# we can find the hypotnuse by hypot() method.
print(math.hypot(4,3))
# it just take the co-ordinate and calculate the length of the line from origin to that co-ordinate.

# we have infinite() and isinf() function to determine if a value is finite or infinity.
print(math.isfinite(334))
print(math.isinf(77))
# we can create infinite value by inf attribute.
p=math.inf
print(math.isinf(p))

# isqurt() returns the integer part of the square root of the input.
print(math.isqrt(66))

# we can create nan values with nan attribute.
a=math.nan
# we can examine if it is a nan or not by isnan() method.
print(math.isnan(a))

# we can find the euclidian distance beetween two point in any dimention.
l=[0,10,20,30,5]
r=[0,10,24,3,89]
print(math.dist(l,r))

# using linear algebra we can calculate this manually,
import numpy as np
a1=np.array(l)
a2=np.array(r)

a3=a1-a2

res=0
for elements in a3:
    res += elements**2

print(np.sqrt(res))

# we can find the number of combination using comb() method.
n=10
r=4
print(math.comb(n,r))

# we can find the number of permutation using perm() method.
n=10
r=4
print(math.perm(n,r))

# copysign() returns the magnitute(value) of first arguement and sign(+-) of second arguement.
print(math.copysign(20.56,-56.7))

# we haave some more functions and constants in math module.
# we will use them later if needed.