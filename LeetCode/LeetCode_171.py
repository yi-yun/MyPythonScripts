class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        a = len(s)
        sum=0
        for i in s:
            sum += (ord(i) - 64) * 26 **(a-1)
            a -= 1
        print(sum)

Solution().titleToNumber('ZY')