class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A
        
        left = 0
        right = len(A) - 1
        half = (len(A) + len(B)) // 2

        while True:
            i = (left + right) // 2 #mid of A
            j = half - i - 2 #mid of B

            Aleft = A[i] if i >= 0 else float("-infinity")
            Aright = A[i+1] if (i+1) < len(A) else float("infinity")
            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j+1] if (j+1) < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2:
                    return min(Aright, Bright)
                
                else:
                    return (min(Aright, Bright) + max(Aleft, Bleft)) / 2
                
            elif Aleft > Bright:
                right = i - 1
            else:
                left = i + 1

nums1 = [1,2]
nums2 = [3,4]


print(Solution().findMedianSortedArrays(nums1, nums2))
