def func(index, flag, numbers, result):
    # flag=True means you are independent to choose 0/1
    # flag=False means you could only choose 0
    if index >= len(numbers):
        result.append(''.join(map(str, numbers)))
        return
    numbers[index] = "0"
    func(index + 1, True, numbers, result)
    if flag == True:
        numbers[index] = '1'
        func(index + 1, False, numbers, result)
        numbers[index] = '0'

def generateBinaryStrings(n):
    numbers = [0] * n
    result = []
    func(0, True, numbers, result)
    return result

# Example usage
print(generateBinaryStrings(3))
