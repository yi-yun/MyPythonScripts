class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        # return s.reverse()
        length = len(s)
        for i in range(length//2):
            if s[i] != s[length - 1 - i]:
                s[i], s[length - 1 - i] = s[length - 1 - i], s[i]
        return s


print(Solution().reverseString(["h", "a", "n", "n", "a", "H"]))
