x = [1, 2, 3, 4, 1, 2, 6, 4, 4, 5]
def bubble(num):
    n = len(num)
    for i in range(n):
        for j in range(0, n - i - 1):
            if num[j] > num[j + 1]:
                num[j], num[j + 1] = num[j + 1], num[j]
    return num
print(bubble(x))
