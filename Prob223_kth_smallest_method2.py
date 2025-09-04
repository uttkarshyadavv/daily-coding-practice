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
        count = [0]   # mutable container
        ans = [None]

        def inorder(node):
            if node is None or ans[0] is not None:
                return
            inorder(node.left)
            count[0] += 1
            if count[0] == k:
                ans[0] = node.val
                return
            inorder(node.right)

        inorder(root)
        return ans[0]
