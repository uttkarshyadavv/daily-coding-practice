num=[1,2,3,4,5,56,6]   #This num[:] means in place change, No any need new space
num[:]= [num[len(num)-1]]+ num[:len(num)-1]
print(num)
