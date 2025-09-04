class Solution(object):
    def kthLargest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        count = [0]   # mutable counter
        ans = [None]

        def inorder(node):
            if node is None or ans[0] is not None:
                return
            inorder(node.right)          # bigger values first
            count[0] += 1
            if count[0] == k:            # k-th largest found
                ans[0] = node.val
                return
            inorder(node.left)

        inorder(root)
        return ans[0]
