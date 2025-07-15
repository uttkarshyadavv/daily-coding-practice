def para(i,n):
    if i==n:
        print(1)
        return
    print(n)
    para(i,n-1)
para(1,4)
