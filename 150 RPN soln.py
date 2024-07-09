class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []

        for token in tokens:
            if not token in '+-/*':
                stack.append(int(token))
            else:
                a = int(stack[-1])
                stack.pop()
                b = int(stack[-1])
                stack.pop()
                
                if token == '+':
                    val = a + b
                elif token == '-':
                    val = a-b
                elif token == '*':
                    val = a*b
                elif token == '/':
                    val = int(a/b)
                stack.append(val)
        return stack[0]
    

tokens = ["4","13","5","/","+"]

print(Solution().evalRPN(tokens))

