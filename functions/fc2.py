def even_odd():
    num=int(input("Enter the number:"))
    i=0
    while i<=num:
        if num%2==0:
            print("The given number is even")
        else:
            print("The given number is odd")
        break