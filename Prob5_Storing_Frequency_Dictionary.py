nums= [1,1,5,7,2,1,8,9,6,6,3,5]
n=nums
freq={}
for i in range (0,len(n)):
    if n[i] in freq:
        freq[n[i]]+=1
    else:
        freq[n[i]]=1
print(freq)
