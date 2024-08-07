class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[left]

        while left <= right:
            if nums[left] < nums [right]:
                result = min(result, nums[left])
                break

            mid = (left + right) // 2

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1

        return result



nums = [3, 4, 5, 1, 2]
print(Solution().findMin(nums))