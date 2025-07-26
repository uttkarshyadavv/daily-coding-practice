# Prob55: Leaders in an Array using Two Pointer approach
# A leader is an element that is greater than or equal to all elements to its right.

arr = [5, 10, 20, 40]
n = len(arr)
leader = []
i = 0
j = 1

while i < n and j < n:
    if arr[i] < arr[j]:
        i += 1
        j = i + 1
    elif arr[i] >= arr[j]:
        if j == n - 1:
            leader.append(arr[i])
            i += 1
            j = i + 1
        else:
            j += 1

leader.append(arr[n - 1])
print(leader)
