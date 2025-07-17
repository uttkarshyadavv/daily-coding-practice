arr=[1,2,3,4]
arr2=[0]*len(arr)
def rev(i,n):
    global arr
    global arr2
    if i==n:
        print(arr2)
        return
    arr2[i]=arr[n-i-1]
    rev(i+1,n)
rev(0,4)
