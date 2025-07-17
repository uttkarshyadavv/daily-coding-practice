arr=[5,7,3,2,6,1,5,9]
def rev(arr,left,right):
    if left>=right:
        print(arr)
        return
    arr[left],arr[right]=arr[right],arr[left]
    rev(arr,left+1,right-1)
rev(arr,0,7)
