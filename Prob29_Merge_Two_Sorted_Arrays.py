x = [1, 2, 3, 4, 4]
y = [2, 3, 4, 45, 67, 100]
def merge_arr(x, y, result):
    i, j = 0, 0
    n, m = len(x), len(y)
    while i < n and j < m:
        if x[i] <= y[j]:
            result.append(x[i])
            i += 1
        else:
            result.append(y[j])
            j += 1
    while i < n:
        result.append(x[i])
        i += 1
    while j < m:
        result.append(y[j])
        j += 1
    return result
print(merge_arr(x, y, []))
