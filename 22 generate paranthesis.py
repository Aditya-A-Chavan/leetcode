class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        result = []
        #add an open paranthesis only if open < n
        #add an close paranthesis only if open > close
        #WILL BE VALID IF AND ONLY IF close == open == n

        def inner_reccur(openN, closedN):
            if openN == closedN == n:
                result.append("".join(stack))
                # print("result", stack)
                return
            
            if openN < n:
                stack.append("(")                
                inner_reccur(openN + 1, closedN)
                # print("openN", stack)
                stack.pop()
                # print("openN", stack)
            
            if closedN < openN:
                stack.append(")")
                inner_reccur(openN, closedN + 1)
                # print("closedN", stack)
                stack.pop()
                # print("closedN", stack)
        
        inner_reccur(0, 0)

        return result
    
print(Solution().generateParenthesis(3))