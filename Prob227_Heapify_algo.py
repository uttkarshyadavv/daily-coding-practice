#Heapify Algorithm is of two types 1) Heapify Up 2) Heapify Down
#Heapify down --> Move it in the side where the number is greater. If tree.left>tree.right move the node value to the left
#Heapify Up --> One direction is their only no need to worry
##CODE FOR MAX HEAP
def heapify (arr,index,val):
    if arr[index]>val:
        arr[index]=val
        heapify_down()
    else:
        arr[index]=val
        heapify_up()
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
def heapify_up(self,arr,ind):
    parent_Ind=(ind-1)//2
    #if current index holds larger value than the parent
    if ind>0 and arr[ind]>arr[parent_Ind]:
        arr[ind],arr[parent_Ind]= arr[parent_Ind],arr[ind]
        self.heapify_up(arr,parent_Ind)
