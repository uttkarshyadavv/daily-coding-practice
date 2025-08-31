def Lremove(self, n):
    curr = self.head
    count = 0

    # Step 1: Count total nodes
    while curr is not None:
        count += 1
        curr = curr.next

    # Step 2: If removing the head node
    if n == count:
        self.head = self.head.next
        return self.head

    # Step 3: Remove (count - n)th node
    curr = self.head
    index = 0
    while curr is not None:
        if index == count - n - 1:
            if curr.next is not None:
                curr.next = curr.next.next
            break
        curr = curr.next
        index += 1

    return self.head
