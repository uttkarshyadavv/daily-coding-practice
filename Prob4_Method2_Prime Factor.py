n=20
num=n
count=2
for i in range (2,int((num/2)+1),1):
    if num%i==0:
        count+=1
print(count)
