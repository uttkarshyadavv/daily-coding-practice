def nat(sum,i,n):
    if i>n:
        print(sum)
        return
    nat(sum+i,i+1,n)
nat(0,1,4)
