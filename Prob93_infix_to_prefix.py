class Solution:
    def precedence(self, ch):
        if ch == "+" or ch == "-":
            return 1
        if ch == "*" or ch == "/":
            return 2
        if ch == "^":
            return 3
        return 0

    def Infixtoprefix(self, s):
        # reverse the string and swap brackets
        r = ""
        for ch in s[::-1]:
            if ch == "(":
                r += ")"
            elif ch == ")":
                r += "("
            else:
                r += ch

        stack = []
        result = []

        # go through reversed string
        for char in r:
            if ("a" <= char <= "z") or ("A" <= char <= "Z") or ("0" <= char <= "9"):
                result.append(char)
            elif char == "(":
                stack.append(char)
            elif char == ")":
                while stack and stack[-1] != "(":
                    result.append(stack.pop())
                stack.pop()
            else:  # operator
                while stack and self.precedence(stack[-1]) >= self.precedence(char):
                    if char == "^" and self.precedence(stack[-1]) == self.precedence(char):
                        break
                    result.append(stack.pop())
                stack.append(char)

        while stack:
            result.append(stack.pop())

        # reverse result for prefix
        return "".join(result[::-1])