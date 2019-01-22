import heapq 
class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(matrix)
        temp = [(matrix[0][0], 0, 0)]
        ans = None
        for _ in range(k):
            ans, i, j = heapq.heappop(temp)
            if j == 0 and i + 1 < n:
                heapq.heappush(temp, (matrix[i + 1][j], i + 1, j))
            if j + 1 < n:
                heapq.heappush(temp, (matrix[i][j + 1], i, j + 1))
        return ans

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
print(Solution().kthSmallest(matrix,k))
            