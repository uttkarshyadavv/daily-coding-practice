class Solution:
    def postTopre(self,s):
        stack=[]
        for char in s:
            # if character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                #Pop two operands
                operand2= stack.pop()
                operand1= stack.pop()
                #Combine operands with a operator
                new_exp= f"({char}{operand1}{operand2})"
                #Push the result back onto the stack
                stack.append(new_exp)
        #The final element in the stack is the infix expression
        return stack[-1]