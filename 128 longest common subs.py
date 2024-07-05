def solution(nums:list[int]) -> int:
    numSet = set(nums)
    longest = 0
    
    if len(nums) ==0:
        return 0
    for num in nums:
        if num-1 not in numSet:
            length = 0
            while num +length in numSet:
                length += 1
            longest = max(longest, length)
    return longest
                
nums = [100, 4, 200, 1, 3, 2]
print(solution(nums)) # 4