n=121
num=n
rev=0
while num>0:
    digit=num%10
    rev=rev*10+digit
    num=num//10  
if rev==n:
    print("true")
else:
    print("false")
