class Node:
    def _init_(self, val):
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def _init_(self):
        self.head = None

    # Append at tail (insert at end)
    def append(self, val):
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = new_node
        new_node.prev = current
