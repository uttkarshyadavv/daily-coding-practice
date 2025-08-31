def reverse(self, n):
    prev=None
    temp=self.head
    while temp is not None:
        front=temp.next
        temp.next=prev
        prev=temp
        temp=front
