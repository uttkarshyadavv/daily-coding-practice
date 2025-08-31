class DoublyLinkedList:
    def duplicate(self):
        curr=self.head
        while curr is not None:
            if curr.prev== self.head and curr!= self.head:
                curr.prev= None
                self.head = curr
            if curr.prev==curr:
                curr.prev.prev.next= curr
                curr.prev= curr.prev.prev
            curr= curr.next
