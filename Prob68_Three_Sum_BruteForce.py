arr = [-1, 0, 1, 2, -1, -4]
n = len(arr)
triplets = []
i = 0

while i < n:
    j = i + 1
    while j < n:
        k = j + 1
        while k < n:
            if arr[i] + arr[j] + arr[k] == 0:
                temp = sorted([arr[i], arr[j], arr[k]])
                if temp not in triplets:
                    triplets.append(temp)
            k += 1
        j += 1
    i += 1

print(triplets)
