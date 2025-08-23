s="CADBZABCD"
n=len(s)
freq={}
stack=[]
max=0
for i in range(0,n):
    if s[i] not in freq:
        freq[s[i]]=1
        stack.append(s[i])
    else:
        if max<len(stack):
            max=len(stack)
        freq={}
        stack=[]
print(max)
        

    

