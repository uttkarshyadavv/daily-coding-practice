def cycle(self):
    slow=self.head
    fast=self.head
    while fast is not None or fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    return False
