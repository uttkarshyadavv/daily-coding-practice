def sui(i,n):
    if i==n:
        print(n)
        return
    sui(i,n-1)
    print(n)
sui(1,9)
