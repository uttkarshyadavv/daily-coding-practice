class Solution:
    def nge(self, s):
        n = len(s)
        ans = [-1] * n
        stack = []

        for i in range(n - 1, -1, -1):
            if len(stack) == 0:   # if stack empty
                ans[i] = -1
                stack.append(s[i])

            elif s[i] < stack[-1]:   # top is next greater
                ans[i] = stack[-1]
                stack.append(s[i])

            else:   # pop until stack empty or greater found
                while stack and s[i] >= stack[-1]:
                    stack.pop()
                if len(stack) == 0:
                    ans[i] = -1
                else:
                    ans[i] = stack[-1]
                stack.append(s[i])

        return ans
