def middle(self,n):
        curr=self.head 
        while curr is not None:
            n+=1
            curr=curr.next
        curr=self.head
        for i in range(0,n//2):
            curr=curr.next
        return curr
