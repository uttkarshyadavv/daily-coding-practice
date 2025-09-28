import heapq
class KthLargest:
    def __init__(self, k):
        self.k = k
        self.minheap = []  # store k largest elements
    def add(self, val):
        if len(self.minheap) < self.k:
            heapq.heappush(self.minheap, val)
        else:
            if val > self.minheap[0]:
                heapq.heapreplace(self.minheap, val)
        return self.minheap[0] if len(self.minheap) == self.k else None