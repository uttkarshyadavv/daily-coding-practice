n = [1, 6, 7, 3, 8, 2, 6, 5]
def insert(num):
    n = len(num)
    for i in range(1, n):  # start from index 1
        key = num[i]
        j = i - 1
        while j >= 0 and num[j] > key:
            num[j + 1] = num[j]
            j -= 1
        num[j + 1] = key
    return num
print(insert(n))
