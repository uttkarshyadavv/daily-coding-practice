arr = [2, 4, 7, 6, 10, 9, 11, 9]  # min-heap
n = len(arr)

def heapify_down(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_down(arr, n, largest)

# Convert min-heap to max-heap
for i in range(n//2 - 1, -1, -1):
    heapify_down(arr, n, i)

print(arr)  # now arr is a max-heap
