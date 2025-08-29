class Meeting:
    def __init__(self,start,end,position):
        #Sort By ending Time
        self.start=start
        self.end=end
        self.position=position
        n=len(start)
        meet=[Meeting(start[i],end[i],i+1)for i in range(n)] 
        meet.sort(key=lambda x:(x.end,x.start))
        result=[]
        count=1
        lasttime=meet[0].end
        for i in range(1,n):
            if meet[i].start>lasttime:
                count+=1
                result.append(position)
                lasttime=meet[i].end