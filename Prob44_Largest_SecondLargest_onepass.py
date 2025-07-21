x=[55,97,-55,87,95,6]
largest=float('-inf')
s_largest=float('-inf')
n=len(x)
for i in range (0,n):
    if x[i]>largest :
       s_largest=largest
       largest=x[i]
    elif x[i]>s_largest and x[i]!=largest:
        s_largest=x[i]
print(largest)
print(s_largest)
