class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        ans=0
        cnt = {}
        for a in A:
            for b in B:
                cnt[a + b] += 1
        for c in C:
            for d in D:
                ans += cnt[-(c + d)]
        return ans