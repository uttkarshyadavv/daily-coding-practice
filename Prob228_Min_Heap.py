def heapify (arr,index,val):
    if arr[index]>val:
        arr[index]=val
        heapify_up()
    else:
        arr[index]=val
        heapify_down()
def heapify_down(self,arr,ind):
    n=len(arr)
    smallest_Ind= ind
    leftChild_Ind= 2*ind+1
    rightChild_Ind= 2*ind+2
    # If the left child holds larger value, update the largest index
    if leftChild_Ind<n and arr[leftChild_Ind]<arr[smallest_Ind]:
        smallest_Ind=leftChild_Ind
    # if the right child holds larger value, update the largest index
    if rightChild_Ind<n and arr[rightChild_Ind]<arr[smallest_Ind]:
        smallest_Ind=rightChild_Ind
    # if largest is not the current index, swap and heapify down
    if smallest_Ind != ind:
        arr[smallest_Ind],arr[ind]= arr[ind],arr[smallest_Ind]
        self.heapifyDown(arr,smallest_Ind)
def heapify_up(self,arr,ind):
    parent_Ind=(ind-1)//2
    #if current index holds larger value than the parent
    if ind>0 and arr[ind]<arr[parent_Ind]:
        arr[ind],arr[parent_Ind]= arr[parent_Ind],arr[ind]
        self.heapify_up(arr,parent_Ind)
