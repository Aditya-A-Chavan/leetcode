class Solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        water = 0
        lmax = height[left]
        rmax = height[right]

        


        if not height: return 0
 
        while left < right:
            if height[left] < height[right]:
                left+=1
                lmax = max(lmax, height[left])
                water += lmax - height[left]         

            else:
                right -=1
                rmax = max(rmax, height[right])
                water += rmax - height[right]

        return water
    
height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(Solution().trap(height))