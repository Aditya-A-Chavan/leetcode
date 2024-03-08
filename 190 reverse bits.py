# Reverse bits of a given 32 bits unsigned integer.


class Solution:
    def reverseBits(self, n: int) -> int:
        result  = 0
        for _ in range(32):
            result = (result << 1) | (n & 1)
            n >>=1
        return result

        