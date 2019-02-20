class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        S = sum([i for i in A if i % 2 == 0])
        res = []
        for x, k in queries:
            if A[k] % 2 == 0:
                S -= A[k]
            A[k] += x
            if A[k] % 2 == 0:
                S += A[k]
            res.append(S)
        return res


A = [1, 2, 3, 4]
queries = [[1, 0], [-3, 1], [-4, 0], [2, 3]]
print(Solution().sumEvenAfterQueries(A, queries))
