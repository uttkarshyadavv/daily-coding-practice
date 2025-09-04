#Inorder/Preorder
#Good for Space Complexity
class Solution:
    def inorderTraversal(self,root):
        result=[]
        current=root

        while current is not None:
            #Case1: Current has No Left child
            if current.left is None:
                result.append(current.val)
                current=current.right
            else:
                #Case2: Current has left child
                #Find the inorder predecessor
                predecessor=current.left

                #Go to the rightmost node in left subtree
                # or find the node whose right child is current
                while (predecessor.right is not None and predecessor.right!=current):
                    predecessor=predecessor.right

                #Make current as right child of predecessor
                if predecessor.right is None:
                    predecessor.right=current
                    current=current.left
                else:
                    #revert the changes: remove the right child link
                    predecessor.right=None
                    result.append(current.val)
                    current=current.right
        return result