class Solution(object):
    def shoppingOffers(self, price, special, needs):
        """
        :type price: List[int]
        :type special: List[List[int]]
        :type needs: List[int]
        :rtype: int
        """
        #      price,   special,            needs
        # [2,3,4], [[1,1,0,4],[2,2,1,9]], [1,2,1]
        memo = {0: 0}

        def needs2num(n):
            x = 0
            for num in n:
                x = x * 10 + num
            return x

        def dfs(dfs_needs):
            num = needs2num(dfs_needs)
            if num in memo:
                return memo[num]
            cost = 0
            for i in range(len(dfs_needs)):
                cost += dfs_needs[i] * price[i]
            for s in special:
                if s[-1] >= cost:
                    continue
                next_need = []
                for i in range(len(dfs_needs)):
                    ans = dfs_needs[i] - s[i]
                    if ans < 0:
                        next_need = []
                        break
                    next_need.append(ans)
                if len(next_need) == 0:
                    continue
                cost = min(cost, s[-1] + dfs(next_need))
            memo[num] = cost
            return cost
        return dfs(needs)
