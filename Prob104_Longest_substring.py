s = "au"
n = len(s)
freq = {}
stack = []
maxlen = 0
for i in range(n):
    if len(s) == len(set(s)):
        maxlen = len(s)
        break
    if s[i] not in freq:
        freq[s[i]] = 1
        stack.append(s[i])
    else:
        if maxlen < len(stack):
            maxlen = len(stack)
        freq = {}
        stack = []
        freq[s[i]] = 1
        stack.append(s[i])
if maxlen < len(stack):
    maxlen = len(stack)
print(maxlen)


        

    

