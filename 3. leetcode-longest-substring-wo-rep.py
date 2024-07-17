class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        left = 0
        res = 0

        for r in range(len(s)):
            while s[left] in charset:
                charset.remove(s[left])
                l+=1
            charset.add(s[r])
            res = max(res, left - r + 1)


        return res
s = "abcabcbb"

print(Solution().lengthOfLongestSubstring(s))