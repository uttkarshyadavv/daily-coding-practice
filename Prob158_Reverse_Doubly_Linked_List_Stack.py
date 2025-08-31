def reverse(self):
    curr=self.head
    stack=[]
    while curr is not None:
        stack.append(curr.val)
        curr=curr.next
    curr=self.head
    while curr is not None:
        e=stack.pop()
        curr.val=e
        curr=curr.next
        return self.head
