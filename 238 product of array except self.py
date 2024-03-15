# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        result = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * nums[i - 1]

        for k in range(n-2, -1,-1):
            suffix[k] = suffix[k + 1] * nums[k + 1]
        
        for j in range(n):
            result[j] = suffix[j]*prefix[j]

        return result