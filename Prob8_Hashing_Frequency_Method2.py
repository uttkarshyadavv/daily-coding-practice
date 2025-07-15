n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
freq={}
freq2={}
for i in n:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
for j in m:
    if j in freq:
        freq2[j]=freq[j]
    else:
        freq2[j]=0
print(freq2)
