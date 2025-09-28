arr=[2,4,7,6,10,9,11,9]
n=len(arr)
def heapify_up(self,arr,ind):
    parent_Ind=(ind-1)//2
    #if current index holds larger value than the parent
    if ind>0 and arr[ind]<arr[parent_Ind]:
        arr[ind],arr[parent_Ind]= arr[parent_Ind],arr[ind]
        self.heapify_up(arr,parent_Ind)
for i in range(n):
    heapify_up(arr,i)