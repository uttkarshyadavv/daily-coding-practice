class DoublyLinkedList:
    def sum(self, target):
        result = []
        left = self.head
        right = self.head
        while right.next is not None:
            right = right.next
        while left is not None and right is not None:
            s = left.val + right.val  # use .val
            if s == target:
                result.append([left.val, right.val])
                left = left.next      # move left forward
                right = right.prev    # move right backward
            elif s < target:
                left = left.next
            elif s > target:
                right = right.prev
        return result
