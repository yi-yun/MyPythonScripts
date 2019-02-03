class Solution:
    # def peakIndexInMountainArray(self, A):
    #     """
    #     :type A: List[int]
    #     :rtype: int
    #     """
    #     low = 0
    #     higt = len(A)-1
    #     while low < higt:
    #         med = (low + higt) // 2
    #         if med == len(A)-1:
    #             return len(A)-1
    #         elif A[med-1] < A[med] and A[med] > A[med+1]:
    #             return med
    #         elif A[med-1] > A[med]:
    #             higt = med - 1
    #         else:
    #             low = med + 1
    #     return low

    def peakIndexInMountainArray(self, A):
        low, high = 0, len(A) - 1
        while low <= high:
            mid = (high - low) // 2 + low
            if mid in (0, len(A) - 1):
                return mid
            elif A[mid] > A[mid - 1] and A[mid] > A[mid + 1]:
                return mid
            elif A[mid] < A[mid - 1]:
                high = mid - 1
            else:
                low = mid + 1
        return -1


print(Solution().peakIndexInMountainArray([1, 2, 3, 2, 1]))
