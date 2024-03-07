class solution:
    def integerBreak(self, n:int) -> int:
        dp = {} #intiializing cahceeeee that is, dynamic programming memorization

        def dfs(num):
            if num in dp:
                return dp[num] # base conditon that if solution already exists in dp, return the solution instead of going in loop
            
            if num == 1:
                return 1


            # dp[num] = 0  if n == num else num #what this does is that is prevents the broken up values to be broken up further
            res = 0
            for i in range (1, num):
                val = dfs(i) * dfs(num-1) #makes sure that the sum of broken number is the n input number
                res = max(dp[num], val)
            
            dp[max] = res
            return res
        return dfs(n)