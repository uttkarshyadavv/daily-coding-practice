def solve(index,total,bracket,result):
    if index>=len(bracket):
        if total==0:
            result.append("".join(bracket))
        return 
    if total>len(bracket)//2:
        return
    elif total<0:
        return
    bracket[index]="("
    sum=total+1
    solve(index+1,sum,bracket,result)
    bracket[index]=")"
    sum=total-1
    solve(index+1,sum,bracket,result)
