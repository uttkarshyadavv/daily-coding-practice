n=123
num=n
sum1=0
while num>0:
    digit=num%10
    cube= digit*digit*digit
    sum1=sum1+cube
    num=num//10
if n==sum1:
    print("Congrats! It's a Armstrong Number")
else:
    print("Not a Armstrong Number")
