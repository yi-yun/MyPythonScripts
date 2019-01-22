# class Solution:
#     def nthSuperUglyNumber(self, n, primes):
#         """
#         :type n: int
#         :type primes: List[int]
#         :rtype: int
#         """
#         res=[1]
#         if n == 0:
#             return None
#         if n==1:
#             return res[0]
#         while len(res) < n:
#             yy = []
#             for i in primes:
#                 for j in res:
#                     temp=i*j
#                     if temp > res[-1]:
#                         yy.append(temp)
#                         break
#             res.append(min(yy))
#         return res[-1]
class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        candidates = [1]*len(primes)
        ids = [0]*len(primes)
        superNums = [1]
        nextMin = 1
        for count in range(1, n) :
            for i in range(len(primes)) :
                if nextMin == candidates[i] :
                    candidates[i] = superNums[ids[i]]*primes[i]
                    ids[i] += 1
            nextMin = min(candidates)
            superNums.append(nextMin)
        return superNums[-1]


n=100000
primes=[7,19,29,37,41,47,53,59,61,79,83,89,101,103,109,127,131,137,139,157,167,179,181,199,211,229,233,239,241,251]

print(Solution().nthSuperUglyNumber(n, primes))
