class Solution:
    def __init__(self):
        self.arr=[]
        self.count=0    
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
    def initializeHeap(self):
        self.arr.clear()
        self.count=0
    def insert(self,key):
        self.arr.append(key)
        self.heapify_up(self.arr, self.count)
        self.count+=1
    def changeKey(self,index, new_val):
        if self.arr[index]<new_val:
            self.arr[index]=new_val
            self.heapify_up(self.arr,index)
        else:
            self.arr[index]=new_val
            self.heapify_down(self.arr,index)
    def extractMax(self):
        if self.count==0:
            return None
        ele= self.arr[0]
        self.arr[0], self.arr[self.count-1]= self.arr[self.count-1], self.arr[0]
        self.arr.pop()
        self.count -=1
        if self.count>0:
            self.heapify_down(self.arr,0)
        return ele
    def isEmpty(self):
        return self.count==0
    def getMax(self):
        return self.arr[0] if self.count>0 else None
    def heapSize(self):
        return self.count