#Mechanism: FIFO (First In First Out)
#Queues
#Operations: enqueue(), size(), front(),rear(), dequeue(), is_empty()
class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if len(self.items)==0:
            return "Empty Queue"
        x=self.items.pop(0)
        return x
    def front(self):
        if len(self.items)==0:
            return "Empty Queue"
        return self.items[0]
    def rear(self):
        if len(self.items)==0:
            return "Empty Queue"
        return self.items[-1]
    def size(self):
        return len(self.items)


