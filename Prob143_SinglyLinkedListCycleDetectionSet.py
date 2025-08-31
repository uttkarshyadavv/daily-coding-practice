def cycle():
    curr=curr.head
    my_set=set()
    while curr is not None:
        if curr in my_set():
            return True
        my_set.add(curr)
        curr=curr.next
    return False
