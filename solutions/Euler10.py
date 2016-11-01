from math import sqrt

found = [2]
number = 3

def is_prime(n):
    for num in found:
        if num <= sqrt(n):
            if n%num == 0:
                return False
        else:
            return True

while number < 2000000:
    if is_prime(number):
        found.append(number)
        
    number += 2

print(sum(found))
