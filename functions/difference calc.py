def calc_diff(*x):
    diff = x[0]
    for i in x[1:]:
        diff =diff- i
    print(diff)

calc_diff(100,50,0)


