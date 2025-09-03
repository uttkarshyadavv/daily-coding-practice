#Priority Order: Right->Root->Left
#Reverse Post Order
def solution(root,level,ans):
    if root is None:
        return
    if len(ans)==level:
        ans.append(root.val)
    if root.right:
        solution(root.right,level+1)
    if root.left:
        solution(root.left,level+1)
ans=[]
solution(5,0,ans)
print(ans)
