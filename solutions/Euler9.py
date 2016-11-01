max = 1000
for x in range(1,int(max/3)):
    for y in range(x+1,2*int(max/3)):
        z = max-x-y

        if x**2+y**2 == z**2:
            print(x*y*z)
