from math import log10

def fibo():
    a,b = 1,1

    while True:
        a,b = b, a+b
        yield a

fib = enumerate(fibo(),2)
number = 1

while(int(log10(number))+1 != 1000):
    index,number = next(fib)

print(index)
