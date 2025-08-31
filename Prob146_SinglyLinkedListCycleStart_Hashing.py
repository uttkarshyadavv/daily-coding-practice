def cycle(self):
    curr=self.head
    my_set=set()
    while curr is not None:
        if curr in my_set:
            return curr
        else:
            my_set.add(curr)
            curr=curr.next
    return -1
