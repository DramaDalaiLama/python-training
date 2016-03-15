# calculate roots of x^2 - 14x + 40
from __future__ import division
from math import sqrt
from pdb import set_trace

a=int(1)
b=int(-14)
c=int(40)

def discr(a,b,c):
    discr = b**2 - 4*a*c
    #set_trace()
    return(discr)

def calc_roots(a,b,c):
    d = discr(a,b,c)
    if d < 0:
        return("Discriminant < 0, no roots")
    else:
        x_one = (-1*b + d)/(2*a)
        x_two = (-1*b - d)/(2*a)
        return("Roots are {0} and {1}").format(x_one,x_two)

print(calc_roots(a, b, c))
