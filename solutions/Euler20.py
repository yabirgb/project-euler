def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)

number = factorial(100)
print( sum([ int(x) for x in str(number) ]) )
