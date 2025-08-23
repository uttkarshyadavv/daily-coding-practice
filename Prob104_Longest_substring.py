s = "CADBZABCD"
n = len(s)
freq = {}
stack = []
maxlen = 0

for i in range(n):
    if s[i] not in freq:
        freq[s[i]] = 1
        stack.append(s[i])
    elif len(s) == len(set(s)):
        maxlen = len(s)
        break
    else:
        if maxlen < len(stack):
            maxlen = len(stack)
        freq = {}
        stack = []
        freq[s[i]] = 1
        stack.append(s[i])

# final check
if maxlen < len(stack):
    maxlen = len(stack)

print(maxlen)

        

    

