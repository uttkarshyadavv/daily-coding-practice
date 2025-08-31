def paranthesis(n, open_count, close_count, number, result):
    # Base case
    if open_count == n and close_count == n:
        result.append(''.join(number))
        return
    
    # Choice 1: Add "(" if we can
    if open_count < n:
        number.append("(")
        paranthesis(n, open_count + 1, close_count, number, result)
        number.pop()
    
    # Choice 2: Add ")" if we can
    if close_count < open_count:
        number.append(")")
        paranthesis(n, open_count, close_count + 1, number, result)
        number.pop()

def generateParenthesis(n):
    result = []
    paranthesis(n, 0, 0, [], result)
    return result

print(generateParenthesis(3)) 
