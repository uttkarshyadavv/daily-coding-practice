coins=[1,2,5,10,20,50,100,200,500,2000]
target=43
i=0
while i < len(coins):
    if coins[i] > target:
        coins.pop(i)
    else:
        i += 1
print(coins)
freq={}
for i  in range(0,len(coins)):
    if coins[i] not in freq:
        freq[coins[i]]=1
    else:
        freq[coins[i]]+=1
print(freq)
currv=0
remaining=target
used=[]
while remaining>0 and len(coins)>0:
    if coins[-1]<=remaining:
        currv=currv+coins[-1]
        used.append(coins[-1])
        remaining=target-currv
    else:
        while remaining<coins[-1] and len(coins)>0:
            del freq[coins[-1]]
            coins.pop()
print(used)
    

