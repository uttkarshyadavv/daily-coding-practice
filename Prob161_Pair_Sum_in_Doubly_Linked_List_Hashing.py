class DoublyLinkedList:
    def sum(self,target):
        temp=self.head
        my_set=set()
        result=[]
        while temp is not None:
            remaining= target- temp.val
            if remaining in my_set:
                result.append([temp.val,remaining])
            my_set.add(temp.val)
            temp=temp.next
        return result
