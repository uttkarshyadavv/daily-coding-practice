x=[55,97,-55,87,95,6]
largest=float('-inf')
s_largest=float('-inf')
for i in range(0,len(x)):
    largest = max(largest,x[i])
print(largest)
for i in range(0,len(x)):
    if x[i]!=largest and x[i]>s_largest:
        s_largest=x[i]
print(s_largest)
