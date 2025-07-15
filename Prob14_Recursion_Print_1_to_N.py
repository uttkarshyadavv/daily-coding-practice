def sui(i,n):
    if i==n:
        print(n)
        return
    print(i)
    sui(i+1,n )
sui(1,9)
