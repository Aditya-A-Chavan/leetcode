# Given a string s consisting of words and spaces, return the length of the last word in the string.

# A word is a maximal 
# substring
#  consisting of non-space characters only.

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split()
        # last = len(s_list)-1

        # last_word = s_list[last]
        # return len(s_list[last_word])
        return len(s_list[-1])

        