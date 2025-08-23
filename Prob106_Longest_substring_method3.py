def longest_unique_substring(s):
    n = len(s)
    my_dict = dict()
    left = 0
    maxi = 0
    for right in range(n):
        if s[right] in my_dict:
            left = max(left, my_dict[s[right]] + 1)
        maxi = max(maxi, right - left + 1)
        my_dict[s[right]] = right
    return maxi    

    


