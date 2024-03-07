#RUNTIME: 37ms, <94% users



class Solution:
    def romanToInt(self, s: str) -> int:
        roman_val = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000 
        }

        sum = 0
        prev_value = 0

        for char in s:
            current = roman_val[char]

            if current > prev_value:
                sum += current - 2*prev_value
            else:
                sum += current
            prev_value = current
        return sum
        