#It's for every type of character value not just lower digit alphbets
s='azyXyyzRRaaa'
q=['d','a','y','X']
hash = [0]*128
for ch in s:
    ascii=ord(ch)
    hash[ascii]+=1
for ch in q:
    ascii=ord(ch)
    print(hash[ascii])
