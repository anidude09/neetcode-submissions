class Solution:
    def calPoints(self, operations: List[str]) -> int:

        output = []


        for char in operations:
            if char == "+":
                x = output[-1] + output[-2]
                output.append(x)
            elif char == "D":
                x = 2 * int(output[-1])
                output.append(x)
            elif char == "C":
                output.pop()
            else:
                output.append(int(char))
            
        return sum(output)         
            

        