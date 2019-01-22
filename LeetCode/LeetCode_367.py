class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        low, high = 0, num
        while low <= high:
            mid = (low + high) // 2
            temp=mid ** 2
            if temp == num:
                return True
            elif temp < num:
                low = mid + 1
            else:
                high = mid - 1
        return False

print(Solution().isPerfectSquare(16))