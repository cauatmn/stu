__author__ = 'cm'
import  os
#! usr/bin/python
import math
from functools import reduce
L = [['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']]
def quadratic(a,b,c):
    if a == 0:
        return False
    x1 =(((-b)+math.sqrt(b*b-4*a*c))/(2*a))
    x2 = (((-b)-math.sqrt(b*b-4*a*c))/(2*a))
    print x1,x2
    return x1,x2

def power(x=3,n=2):
        s = 1
        while (n>0):
            n = n - 1
            s = s*x
        return s
def f(x):
    return x[:1].upper() + x[1:].lower()

def chengfa(x,y):
    return x*y

def prod(*E):
    return  reduce(chengfa,L)
def normalize(*names):
    r = map(f,names)
    print list(r)
if __name__ =='__main__':
    L1 = ['adam', 'LISA', 'barT']
    L2 = list(map(f,L1))
    print L2
    L =[3,5]
    print prod(L)


