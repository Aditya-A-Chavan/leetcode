class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        combine = [[p, s] for p, s in zip(position, speed)]
        combine.sort()
        stack = []

        for p, s in combine[::-1]:
            time = (target - p)/s
            stack.append(time)

            if len(stack) >= 2 and stack[-1] <= stack [-2]:
                stack.pop()



        return len(stack)
    

    
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(Solution().carFleet(0, position, speed))