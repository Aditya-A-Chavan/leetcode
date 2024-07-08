class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left = 0
        right = n-1

        while left< right:
            while (left < right) and not self.check_for_alphanumeric(s[left]):
                left += 1
            while (left < right ) and not self.check_for_alphanumeric(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True


    def check_for_alphanumeric(self, c):
        return ((ord("A") <= ord(c) <= ord("Z")) or (ord ("a") <= ord(c) <= ord("z")) or (ord('0') <= ord(c) <= ord('9')))
        
