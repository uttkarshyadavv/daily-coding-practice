price=[7,2,1,5,6,4,8]
n=len(price)
min=float('inf')
max=float('-inf')
for i in range(0,n):
    if price[i]<min:
        min=price[i]
    profit=price[i]-min
    if profit>max:
        max=profit
print(min)
print(max)
