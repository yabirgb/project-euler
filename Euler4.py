largest = 0

for primer in range(100,1000):
    for segundo in range(100,1000):
        product = primer*segundo
        if  product > largest and product == int(str(product)[::-1]):
            largest = int(product)

print(largest)
