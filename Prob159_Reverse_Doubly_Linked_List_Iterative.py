def reverse(self):
    curr=self.head
    if self.head.next is None:
        return self.head
    prev= None
    while curr is not None:
        front=curr.next
        curr=curr.next
        curr.prev= front
        prev= curr
        curr= prev
    return prev
