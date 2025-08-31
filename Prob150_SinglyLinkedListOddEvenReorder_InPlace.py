def oddeven(self):
    odd=self.head
    even=odd.next
    even_head=even
    if odd is None or odd.next is None:
        return odd
    while even is not None and even.next is not None:
        odd.next=odd.next.next
        odd= odd.next
        even.next=even.next.next
        even=even.next
    odd.next=even_head
    return self.head
