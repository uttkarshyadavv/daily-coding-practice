#Optimal
def nge(self,s):
        ans=[-1]*len(s)
        stack=[]
        for i in s[::-1]:
            while len(stack)!=0 and stack[-1]<=s[i]:
                stack.pop()
            if len(stack)!=0:
                ans[i]=stack[-1]
            stack.append(s[i])
        return ans

