count=0
sum=0
def sumc(i,n):
    global sum
    if i>n:
        print(sum)
        return
    global count
    count=i**3
    sum+=count
    sumc(i+1,n)
sumc(1,6)
