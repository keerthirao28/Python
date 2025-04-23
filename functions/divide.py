def divide(*x):
    div = x[0]
    for i in x[1:]:
       div =div / i
    print(div)


divide(100, 2, 5)