s = list('uttkarshyadavv')
rev = list(' ' * len(s))
for i in range(0, len(s)):
    rev[i] = s[len(s) - i - 1]
print(str(rev))
print(str(s))
if rev == s:
    print(True)
else:
    print(False)
