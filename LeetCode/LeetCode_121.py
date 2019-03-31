class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        p = 0
        minDay = prices[0]
        for i in range(1, len(prices)):
            minDay = min(minDay, prices[i])
            p = max(p, prices[i] - minDay)
        return p
