class Solution:
    def preToInfix(self,s):
        stack=[]
        for char in s[::-1]:
            # if character is an operand, push it to the stack
            if char.isalnum():
                stack.append(char)
            else:
                #Pop two operands
                operand1= stack.pop()
                operand2= stack.pop()
                #Combine operands with a operator
                new_exp= f"({operand1}{char}{operand2})"
                #Push the result back onto the stack
                stack.append(new_exp)
        #The final element in the stack is the infix expression
        return stack[-1]