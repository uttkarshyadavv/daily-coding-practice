class Solution:
    def nge(self,s):
        result=[]
        for i in range(0,len(s)):
            for j in range(i+1,len(s)):
                if s[j]>s[i]:
                    result.append(s[j])
                    break
                else:
                    result.append(-1)
        return result

