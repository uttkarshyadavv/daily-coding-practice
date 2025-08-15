#Deque Class: Double Ended Queue
#Double-Ended Queue: Its like a Doubly Linked List
#Advantages: O(1) time complexity could be achieved
from collections import deque
stack=deque([])
stack.append(100)
stack.append(200)
stack.append(300)
stack.appendleft(1)
stack.appendleft(9)
stack.pop()
stack.popleft()
print(stack)

