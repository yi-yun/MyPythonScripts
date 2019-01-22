class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        low, high = 0, len(letters) - 1
        while low <= high:
            mid=(low+high)//2
            if letters[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1
        low = 0 if low == len(letters) else low
        return letters[low] 