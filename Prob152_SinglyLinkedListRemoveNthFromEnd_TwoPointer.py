def Lremove(self,n):
    slow=self.head
    fast=self.head
    for _ in range(n):
        fast=fast.next
    if fast is None:
        return self.head.next
    while fast is not None:
        slow=slow.next
        fast=fast.next
    slow.next=slow.next.next
    return self.head
