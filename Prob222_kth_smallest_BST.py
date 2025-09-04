# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        def inorder(node, arr):
            if node is None:
                return
            inorder(node.left, arr)        # visit left first (smaller values)
            arr.append(node.val)           # then root
            inorder(node.right, arr)       # then right

        arr = []
        inorder(root, arr)
        return arr[k-1]
