class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
#we should know the head
class SinglyLinkedList:
    def __init__(self):
        self.head=None
    def traversal(self):
        if self.head is None:
            print('SLL is empty')
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end="")
                curr=curr.next