def cycle(self):
    slow=self.head
    fast=self.head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return slow
    return None
