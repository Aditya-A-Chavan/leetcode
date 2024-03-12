# You are given two strings order and s. All the characters of order are unique and were sorted in some custom order previously.

# Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs before a character y in order, then x should occur before y in the permuted string.

# Return any permutation of s that satisfies this property.

class Solution:
    def customSortString(self, order: str, s: str) -> str:
        MAX_CHAR = 26  
        count = [0] * MAX_CHAR
        
       
        for char in s:
            count[ord(char) - ord('a')] += 1
        
        result = ""
        
       
        for char in order:
            result += char * count[ord(char) - ord('a')]
        
        
        for char in s:
            if char not in order:
                result += char
        
        return result
