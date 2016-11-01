prev = 1

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b, a%b)

def lcm(a,b):
    greatest = gcd(a,b)

    return (a/greatest)*b

for n in range(1,21):
    prev = lcm(prev,n)

print(int(prev))
