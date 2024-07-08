class solution:
    def two_sum(self, numbers: list[int], target: int) -> list[int]:
        left = 0 
        right = len(numbers) - 1

        while left < right:
            current = numbers[left] + numbers[right]

            if current == target:
                return [left+1, right+1]        
            elif current > target:
                right -= 1
            else:
                left += 1
        return []
    

numbers = [2,7,11,15]
target = 9
print(solution().two_sum(numbers, target)) # [1,2]