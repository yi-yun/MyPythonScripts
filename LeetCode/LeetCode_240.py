class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # [[5]]
        if len(matrix) > 0 and len(matrix[0]) > 0:
            y = len(matrix[0]) - 1
            for x in range(len(matrix)):
                while y and matrix[x][y] > target:
                    y -= 1
                if matrix[x][y] == target:
                    return True
        return False


list1 = [[-1, 3]]
list2 = [[5]]

print(Solution().searchMatrix(list2, 5))
