class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
#we should know the head
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def append(self,val):
        newnode=Node(val)
        if self.head==None:
            self.head=newnode
#initially the head was empty but we created the newnode variable, where we stored our new value
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newnode