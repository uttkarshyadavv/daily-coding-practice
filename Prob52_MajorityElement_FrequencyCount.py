n=[1,2,3,3,3,1,3]
freq={}
for i in range (0,len(n)):
    if n[i] in freq:
        freq[n[i]]+=1
    else:
        freq[n[i]]=1
    if freq[n[i]]>(len(n)/2):
        print(n[i])
