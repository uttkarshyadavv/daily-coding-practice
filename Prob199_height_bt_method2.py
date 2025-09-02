def solve(node):
    if node ==None:
        return 0
    leftheight=solve(node.left)
    rightheight=solve(node.right)
    return 1+max(leftheight,rightheight)
