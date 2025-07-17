original = "nitin"
s = list(original)

def rev(s, left, right):
    if left >= right:
        return
    s[left], s[right] = s[right], s[left]
    rev(s, left + 1, right - 1)

rev(s, 0, len(s) - 1)

if ''.join(s) == original:
    print("Palindrome")
else:
    print("Not a palindrome")
