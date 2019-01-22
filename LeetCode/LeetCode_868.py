class Solution:
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        sum = 0
        res = []
        str = (bin(N))[2:]
        print(str)
        for i in range(len(str)):
            if str[i] == '1':
                res.append(i-sum)
                sum = i
                
        if len(res) == 1:
            return 0
        elif len(res) == 0:
            return 0
        else:
            return max(res[1:])
print(Solution().binaryGap(8))