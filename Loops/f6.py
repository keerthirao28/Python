a, b = 0, 1
for z in range(10):
    a, b = b, a + b
    print(a, end=" ")
#fibonocci series