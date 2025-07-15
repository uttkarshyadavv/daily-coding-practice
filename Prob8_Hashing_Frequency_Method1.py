#constraint 1=<x[i]=<10 , n and m both can have 10^8 elements

x=[1,2,2,2,3,3,3,4,5,5,3,3,7,8,8,9,9,9,10]
y=[3,4,2,2,5,5,99]     
hash=[0]*11
for i in x:
    hash[i]+=1
for i in y:
    if i<1 and i>10:
        print(0)
    else:
        print(hash[i]) 
