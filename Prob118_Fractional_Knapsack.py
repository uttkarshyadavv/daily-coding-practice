arr=[(100,20),(60,10),(100,50),(200,50)]
#(Value,weight)
weight=90
arr.sort( key=lambda x:x.value/x.wt,reverse=True)
currw=0
finalvalue=0
for i in range(0,len(arr)):
    if currw+arr[i].wt<=weight:
        currw=currw+arr[i].wt
        finalvalue+=arr[i].value
    else:
        remain=weight-currw
        cost=arr[i].value/arr[i].wt*remain
return finalvalue
