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

#len performance is O(1)
#https://goo.gl/1yztpY
while len(found) < 10001:
    if is_prime(number):
        found.append(number)
        
    number += 2

print(found[-1])
