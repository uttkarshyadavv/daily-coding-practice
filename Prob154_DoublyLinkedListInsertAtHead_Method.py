class Node:
    def _init_(self,val):
        self.val=val
        self.prev=None
        self.next=None
class DoubleLinkedList:
    #Insert at Head
    def insert_at_head(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
