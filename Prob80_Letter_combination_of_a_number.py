#old keypad phones mimic
#constraint: The numbers can't be 1,*,0,# and maximum upto 4 digits
def finder(index,subset,digits,result):
    char_map= {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    if index>=len(digits):
        result.append(subset.copy())
        return result
    for ch in char_map[digits[index]]:
        subset.append(ch)
        finder(index+1,subset,digits,result)
        subset.pop()
digits='86'
result=[]
finder(0,[],digits,result)
print(result)




