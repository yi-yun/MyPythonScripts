class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        temp = 0
        for i in nums:
            temp ^= i
        last = self.get_first(temp)
        a, b = 0, 0
        for i in nums:
            if self.confirm(i, last):
                a ^= i
            else:
                b ^= i
        return [a, b]

    def get_first(self, n):
        cnt = 0
        while n & 1 == 0:
            cnt += 1
            n = n >> 1
        return cnt

    def confirm(self, n, t):
        n = n >> t
        return n & 0x01


print(Solution().get_first(1))
