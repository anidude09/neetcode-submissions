class Solution:
    def isValid(self, s: str) -> bool:


        char_dict = { ')' : '(' , ']' : '[' , '}': '{'}

        stack = []

        for char in s:
            if char in char_dict:
                comp = stack.pop() if stack else "#"
                if comp != char_dict[char]:
                    return False
            
            else: 
                stack.append(char)

        return True if not stack else False

       
                
            






        