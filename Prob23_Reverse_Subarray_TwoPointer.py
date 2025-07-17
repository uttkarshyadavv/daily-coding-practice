s = list('uttkarshyadavv')
l = 3
r = 9
while l < r:
    s[l], s[r] = s[r], s[l]
    l += 1
    r -= 1
print(''.join(s))
