def lencycle(self):
    slow=self.head
    fast=self.head
    while fast is not None and fast.next is not None:
        if slow==fast:
            slow= slow.next
            count=1
            while slow!=fast:
                slow=slow.next
                count+=1
        else:
            slow=slow.next 
            fast=fast.next.next
    return 0
