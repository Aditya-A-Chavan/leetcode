# Given an array nums of size n, return the majority element.


# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

#Working: 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1

        return candidate




#NON WORKING: since complexity is n^2
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        # counter = len(nums) 
        max_count = 0

        if (1<=n<=50**4):

            for i in range(n):
                count = 1

                for j in range(i+1, n):
                    if nums[i] == nums[j]:
                        count+=1
            
                if (count > max_count):
                    max_count = count
                    index = i
            
            return nums[index]


