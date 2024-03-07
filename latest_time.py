
from ast import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        result = ""

        for i in range (4):
            for j in range(4):
                for k in range(4):
                    if i == j or j == k or j == i: continue
                    hh = str(arr[i])+str(arr[j])
                    mm = str(arr[k])+str(arr[6-i-j-k])
                    time = hh +":"+mm

                    if hh< 24 and mm < 60 and time > result:
                        return result
        
        return result