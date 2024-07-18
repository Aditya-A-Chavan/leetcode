class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        left = 0
        res = 0
        maxf = 0
        
        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            maxf = max(maxf, count[s[right]])
            
            while (right - left + 1) - maxf > k:
                count[s[left]] -= 1
                left += 1
                
            res = max(res, right - left + 1)
        
        return res

s = "ABABBA"
k = 2
print(Solution().characterReplacement(s, k))