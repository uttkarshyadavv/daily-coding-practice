class DoublyLinkedList:
    def sum(self,target):
        temp1= self.head
        result=[]
        while temp1 is not None:
            temp2= temp1.next
            while temp2 is not None:
                if temp1.val+temp2.val==target:
                    result.append([temp1.val,temp2.val])
                    temp2=temp2.next
            temp1=temp1.next
        return result
