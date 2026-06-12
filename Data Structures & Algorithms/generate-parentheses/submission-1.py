class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        stack = []
        result = []

        def back(op, close): 
            if op == close == n : 
                result.append("".join(stack))
                
            if op < n : 
                stack.append("(")
                back(op + 1, close)
                stack.pop()
            if close < op :
                stack.append(")")
                back(op, close + 1)
                stack.pop()
        
        back(0, 0)
        return result

        






        
        