#stack: Can store any kind of data
#Mechanism: LIFO(Last in first out)
#Basic Operations: push(),pop(),top(): The last element of stack,size()
class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items)==0
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if len(self.items)==0:
            return "Cannot pop, stack is empty"
        x=self.items.pop()
        return x
    def top(self):
        if len(self.items)==0:
            return "Empty stack"
        return self.items[-1]
    def size(self):
        return len(self.items)
stack=Stack()
stack.push(5)
stack.push(10)
stack.push(15)
print(f"Stack content = {stack}")
print(f"Popped content = {stack.pop()}")
print(f"Stack content = {stack}")
print(f"Top Item after pop = {stack.peek()}")
print(f"Stack is empty = {stack.is_empty()}")
