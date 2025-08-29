coins=[1,2,5,10,20,50,100,200,500,2000]
result=[]
n=47
n=len(coins)
for  i in range(n-1,-1,-1):
    while n>=coins[i]:
            result.append(coins)
            n-=coins[i]
print(result)
