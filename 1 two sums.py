# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        
        for i, num in enumerate(nums):
            diffn = target - num
            if diffn in num_dict:
                return [num_dict[diffn], i]
            num_dict[num] = i
        
        return []
