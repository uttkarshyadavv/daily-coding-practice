def oddeven(self):
    value=[]
    temp=self.head
    if temp is None or temp.next is None:
        return temp
    while temp is not None and temp.next is not None:
        value.append(temp)
        temp=temp.next.next
    temp=self.head
    temp=temp.next
    while temp is not None and temp.next is not None:
        value.append(temp)
        temp=temp.next.next
    temp=self.head
    index=0
    while temp is not None:
        temp.val=value[index]
        index+=1
        temp=temp.next
    return self.head
