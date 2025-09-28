arr = [2, 4, 7, 6, 10, 9, 11, 9]
n = len(arr)

def heapify_down(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_down(arr, n, largest)

for i in range(n//2 - 1, -1, -1):
    heapify_down(arr, n, i)

for i in range(n-1, 0, -1):
    arr[0], arr[i] = arr[i], arr[0]  
    heapify_down(arr, i, 0)  

print(arr)  # sorted in ascending order
