class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = triangle[0]
        for i in range(n-2, -1, -1):
            for j in range(i + 1):
                dp[j] = triangle[i][j]+min(dp[j], dp[j+1])
