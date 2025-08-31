#initially the head was empty but we created the newnode variable, where we stored our new value
class Node:
    def _init_(self,val):
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
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=newnode

    def traversal(self):
        if self.head is None:
            print('SLL is empty')
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next
            print()
sll=SinglyLinkedList()
sll.append(20)
sll.append(10)
sll.append(1)
sll.traversal()
