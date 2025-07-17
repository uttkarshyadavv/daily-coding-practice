s='abba'
def palin(s,l,r):
    if l>=r:
        print(True)
        return
    if s[l]!=s[r]:
        print(False)
        return
    else:
        palin(s,l+1,r-1)
palin(s,0,len(s)-1)
