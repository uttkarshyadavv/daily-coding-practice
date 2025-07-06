n=1634
num=n
sum1=0
count=0
while num>0:
    count+=1
    num=num//10
num=n
while num>0:
    digit=num%10
    sum1=sum1+digit**count
    num=num//10
if n==sum1:
    print("Congrats! It's a Armstrong Number")
else:
    print("Not a Armstrong Number")
