# cmath module

# cmath stands for complex math
# it is simmilar as math module, but it has less functions and attributes compared to math module.
# the functions and attributes name are same as math module but they can work with complex number too.

# first we need to import the module 
import cmath

# lets see the directory to find the name of functions and attributes.
print(dir(cmath))

# we can see that here we have:-
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh',
#  'atan', 'atanh', 'cos', 'cosh', 'e', 'exp', 'inf', 'infj', 'isclose', 'isfinite', 'isinf', 'isnan',
#  'log', 'log10', 'nan', 'nanj', 'phase', 'pi', 'polar', 'rect', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau']

# first of all, 
# NOTE that we can even create complex number without cmath module, we can do that by complex() method.
# then we can work with those numbers.
print(complex(2.5,4.5))
# it takes real part as the first arguement and imaginary part as the second arguement
# then it multiply the imaginary part with sqrt of -1 and create the complex number.


# we can see that we have trigonometeric functions.
# sin
# cos
# tan
# asin(arcsin)
# acos(arccos) 
# atan(arctan)

# we also have hyperbolic functions.
# sinh
# cosh
# tanh
# asinh(arcsinh)
# acosh(arccosh)
# atanh(arctanh)

# we also have
# nan
# nanj
        # nanj gives us Complex number with zero real part and NaN imaginary part. 
        # it is Equivalent to complex(0.0, float('nan')).
# isnan
# inf
# infj
        # infj gives us Complex number with zero real part and positive infinity imaginary part 
        # it is Equivalent to complex(0.0, float('inf')).
# isinf
# isfinite

# we have logarithmic function
# log
# log10

# we have some constants
# e
# pie
# tau

# we also have
# sqrt
# exp

# we can print the phase angle of a complex by phase() function.
a=cmath.sqrt(-1)
print(cmath.phase(2+3*a))

# we can Convert a complex from rectangular coordinates to polar coordinatesn using polar() function.
print(cmath.polar(a))

# we can Convert a complex from polar coordinates to rectangular coordinatesn using rect() function.
print(cmath.rect(1.0, 1.5707963267948966))