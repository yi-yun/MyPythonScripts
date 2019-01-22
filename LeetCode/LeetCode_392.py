class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # s_len,t_len=len(s),len(t)
        # i,j=0,0
        # while i < s_len and j < t_len:
        #     if s[i] == t[j]:
        #         i += 1
        #     j += 1
        # return i == s_len
        j=0
        for i in s:
            try:
                res = t.index(i, j)
            except Exception:
                return False
            j += res
        return True

s = "abc"
t = "ahbgdc"
# s = "axc"
# t = "ahbgdc"
print(Solution().isSubsequence(s,t))