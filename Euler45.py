#https://projecteuler.net/problem=45

#Hexagonal numbers are triangolars with and odd index.
#We need to check if hegaxonal number generated is triangular

from itertools import count
from math import sqrt

def pentagonal(number):
    r = (sqrt(1+24*number)+1)/6
    return r == int(r)

for number in count(144):
    check = number*(2*number-1)
    
    if (pentagonal(check)):
        print(number, check)
        break
