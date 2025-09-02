maxi = 0
count = 0
def solution(node):
    global maxi, count
    if node is None:
        maxi = max(maxi, count)
        return
    count += 1
    solution(node.left)
    solution(node.right)
    count -= 1
