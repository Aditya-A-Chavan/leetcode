class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        top = 0
        bottom = ROWS - 1

        while top <= bottom:
            row = (top + bottom) // 2
            if target > matrix[row][COLS-1]:
                top = row + 1
            elif target < matrix[row][0]:
                bottom = row - 1
            else:
                break
        
        if not (top <= bottom):
            return False
    
        row = (top + bottom)//2
        left = 0
        right = COLS - 1

        while left <= right:
            mid = (left + right) // 2

            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right = mid - 1
            else:
                return True
        return False
    
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

print(Solution().searchMatrix(matrix, target))