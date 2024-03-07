#Beats 94.31% of users with Python3


class Solution:
    def minimumLength(self, s: str) -> int:

        left = 0
        right = s.len()-1
        s = s.split()

        while left < right and s[left] == s[right]:
            temp = s[left]

            while (left <= right and s[left] == temp):
                left += 1

            while (left <= right and s[right] == temp):
                right -= 1
        
        return right - left + 1
                

