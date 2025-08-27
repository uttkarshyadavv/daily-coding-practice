g = [2, 6, 8, 1, 4]
s = [4, 2, 7, 1, 2, 3]
g_sort = sorted(g)
s_sort = sorted(s)
print(g_sort) 
print(s_sort)  
left=0
right=0
count=0
while left<len(g_sort) and right<len(s_sort):
    if g_sort[left]<=s_sort[right]:
        count+=1
        left+=1
    else:
        right+=1
print(count)
