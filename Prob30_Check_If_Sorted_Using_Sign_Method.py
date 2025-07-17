x = [10, 20, 30, 40, 50]
n = len(x)
for i in range(n - 2):
    j = i + 1
    if (x[i] - x[j]) * (x[i + 1] - x[j + 1]) < 0:
        print("Not Sorted")
        break
else:
    print("Sorted")
