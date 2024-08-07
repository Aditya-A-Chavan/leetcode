class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i+1, len(nums) -1

            while left < right:
                current = nums[i] + nums[left] + nums [right]
                if current > 0:
                    right -= 1
                elif current < 0:
                    left += 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left += 1
        return result
nums = [-1,0,1,2,-1,-4]
print(Solution().threeSum(nums)) 
                    

