words = ["baa", "abcd", "abca", "cab", "cad"]

i, j = 0, 0
a = len(words)
result = []
b = max(len(word) for word in words)
while i < a and j < b:
    if j < len(words[i]):
        if words[i][j] not in result:
            result.append(words[i][j])
    i += 1
    if i == a - 1:
        i = 0
        j += 1
print(result)

result1 = {ch: idx for idx, ch in enumerate(result)}

for k in range(len(result) - 1):
    if result1[result[k]] > result1[result[k + 1]]:
        print(False)
        break
else:
    print(True)
