class Node:
    def _init_(self,val):
        self.val=val
        self.prev=None
        self.next=None

class DoubleLinkedList:
    #Insert at Head
    def insert(self, val, position):
        new_node= Node(val)
        if self.head is None:
            self.head= new_node
            return
        else:
            curr= self.head
            index=0
            while curr is not None and index< position-1:
                curr=curr.next
                index+=1
            if curr is None:
                print("Poistion out of bounds")
                return
            curr.next=new_node
            new_node.prev=curr
            new_node.next= curr.next
            if curr.next:
                curr.next.prev= new_node
                curr.next= new_node
