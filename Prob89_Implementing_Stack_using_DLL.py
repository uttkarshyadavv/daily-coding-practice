#Implementing Stack Using DLL
#push
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class Doublylinkedlist:
    def __init__(self):
        self.head=None
        self.tail=None
    def push(self,x):
            new_node= Node(x)
            if self.head is None:
                self.head=new_node
                self.tail=new_node
            else:
                self.tail.next=new_node
                new_node.prev=self.tail
                self.tail=new_node
                

