greed=[2,6,8,1,4]
s=[4,2,7,1,2,3]
n=len(s)
result=[]
for i in range(0,len(greed)):
    big=[]
    for j in range(0,len(s)):
        if greed[i]<=s[j]:
            big.append(s[j])
    if big:  
        mini=min(big)
        result.append(mini)
print(len(result))

        
    
