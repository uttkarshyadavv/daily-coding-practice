##IMPORTANT time complexity
arr=[1,8,7,16,11,12,2,4]
n=len(arr)
#If i wanna do that do it for internal nodes not for leaf nodes because leaf nodes have nothing to compare with so they are the biggest
def heapify_down(self,arr,ind):
    n=len(arr)
    largest_Ind= ind
    leftChild_Ind= 2*ind+1
    rightChild_Ind= 2*ind+2
    # If the left child holds larger value, update the largest index
    if leftChild_Ind<n and arr[leftChild_Ind]>arr[largest_Ind]:
        largest_Ind=leftChild_Ind
    # if the right child holds larger value, update the largest index
    if rightChild_Ind<n and arr[rightChild_Ind]>arr[largest_Ind]:
        largest_Ind=rightChild_Ind
    # if largest is not the current index, swap and heapify down
    if largest_Ind != ind:
        arr[largest_Ind],arr[ind]= arr[ind],arr[largest_Ind]
        self.heapifyDown(arr,largest_Ind)
for ind in range((n//2)-1,-1,-1):
    heapify_down(arr,ind)
