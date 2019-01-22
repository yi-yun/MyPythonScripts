class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        low, high = 0, len(numbers) - 1
        while low < high:
            temp=numbers[low] + numbers[high]
            if  temp< target:
                low += 1
            elif temp > target:
                high -= 1
            else:
                return low + 1, high + 1
        return None
