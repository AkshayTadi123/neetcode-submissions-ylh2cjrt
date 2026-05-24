import statistics  

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B)<len(A):
            A, B = B, A

        total_len, half = len(A) + len(B), (len(A) + len(B))//2
        l, r = 0, len(A)-1

        while True:
            mid = (l+r)//2
            diff = half - mid - 2

            A_L = A[mid] if mid>=0 else float("-inf")
            A_R = A[mid+1] if (mid+1)<len(A) else float("inf")
            B_L = B[diff] if diff >=0 else float("-inf")
            B_R = B[diff+1] if (diff+1)<len(B) else float("inf")

            if A_R >= B_L and B_R >= A_L:
                if total_len%2 == 0:
                    return (max(A_L, B_L)+min(A_R, B_R))/2
                else:
                    return min(A_R, B_R)
            elif A_L > B_R:
                r = mid-1
            else:
                l = mid+1


