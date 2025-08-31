#initially the head was empty but we created the newnode variable, where we stored our new value
class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
#we should know the head
class SinglyLinkedList:
    def _init_(self):
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
    def insert(self, val, position):
        newmode=Node(val)
        if position==0:
            newmode.next= self.head
            self.head = newmode
        else:
            current= self.head
            prev_node= None
            count=0
            while current is not None and count< position:
                prev_node=current
                current=current.next
                count+=1 
                prev_node.next= newmode
                newmode.next = current
    def delete(self,val):
        curr= self.head
        if curr.next is not None:
            if curr.val == val:
                self.head=curr.next
                return
            else:
                found= False
                prev= None
                while curr is not None:
                    if curr.val == val:
                        found= True
                        break
                    prev = curr
                    curr=curr.next

                if found:
                    prev.next= curr.next
                    return
                else:
                    print("Node Not Found")
                

sll=SinglyLinkedList()
sll.append(20)
sll.append(10)
sll.append(1)
sll.traversal()
