words = ["baa", "abcd", "abca", "cab", "cad"]
i, j = 0, 0
a = len(words)
result = []

b = max(len(word) for word in words)  # longest word

while i < a and j < b:
    if j < len(words[i]):                # only access if index exists
        if words[i][j] not in result:   # maintain order and uniqueness
            result.append(words[i][j])
    i += 1
    if i == a - 1:
        i = 0
        j += 1
        
print(result)
