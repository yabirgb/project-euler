def fibo(n):
    a,b = 1,1

    while a < n:
        a,b = b, a+b
        yield a

b = sum(filter(lambda x: x%2 == 0, fibo(4000000)))
print(b)
