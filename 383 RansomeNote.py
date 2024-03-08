# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letter_count = {}
        
        for letter in magazine:
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1
        
        for letter in ransomNote:
            if letter not in letter_count or letter_count[letter] == 0:
                return False
            else:
                letter_count[letter] -= 1
        return True