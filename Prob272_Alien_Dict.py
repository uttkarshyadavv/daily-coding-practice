words = ["baa", "abcd", "abca", "cab", "cad"]
i, j = 0, 0
a = len(words)
result = []

b = len(words[0])

while i < a and j < b:
    if j < len(words[i]):
        if words[i][j] not in result: 
            result.append(words[i][j])
    i += 1
    if i == a - 1: 
        i = 0
        j += 1

print(result)

