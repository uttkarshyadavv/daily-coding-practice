bills=[5,5,5,10,20]
n=len(bills)
five,ten=0,0
def solution(bills):
    for i in range(0,n):
        if bills[i]==5:
            five+=1
        elif bills[i]==10:
            if five>=1:
                five-=1
                ten+=1
            else:
                return False
        else:
            if five>=1 and ten>=1:
                five-=1
                ten-=1
            elif five>=3:
                five-=3
            else:
                return False
    return True
        
    