#beats 86.32%

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        try:
            index = haystack.index(needle)
            return index
        except:
            return -1
        