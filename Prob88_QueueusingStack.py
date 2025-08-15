#We have to use two stacks
#Pushing(x): Transfer all elements from stack1 to stack2, Insert element to stack1, Transfer stack2 to stack1
class StackQueue:
    def __init__(self):
        self.st1=[]
        self.st2=[]

    def push(self,x):
        while self.st1:
            self.st2.append(self.st1.pop())
        self.st1.append(x)
        while self.st2:
            self.st2.append(self.st2.pop())

    def pop(self):
        if not self.st1:
            print("Empty Stack")
            return -1
        top_element=self.st1.pop()
        return top_element
    
    def peek(self):
        if len(self.st1)==0:
            print("Empty Stack")
            return -1
        return self.st1[-1]
    
    def is_empty(self):
        return not self.st1

