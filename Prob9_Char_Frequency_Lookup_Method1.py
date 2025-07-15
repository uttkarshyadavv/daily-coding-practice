#ascii value of a=97,b=98,c=99......z=122, Therefore It has a constraint Hence we used the Hashing approach

s='azyxyyzaaaa'
q=['d','a','y','x']
hash=[0]*26
for ch in s:
    ascii=ord(ch)
    index=ascii-97
    hash[index]+=1
for ch in q:
    ascii=ord(ch)
    index=ascii-97
    print(hash[index])
