class Node:
    def _init_(self,val):
        self.val=val
        self.prev=None
        self.next=None
class DoubleLinkedList:
    #Insert at Head
    def append(self,val):
        new_node= Node(val)
        if not self.head:
            self.head= new_node
        else:
            current= self.head
            while current.next is not None:
                current=current.next
                current.next= new_node
                new_node.prev= current   for this
