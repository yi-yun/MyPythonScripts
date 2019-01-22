class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        a = distance([0, 0], target)
        list=[]
        for i in ghosts:
            list.append(distance(i, target))
        for i in list:
            if i <= a:
                return False
        return True
    
def distance(origin, target):
    return abs(origin[0] - target[0]) + abs(origin[1] - target[1])

print(Solution().escapeGhosts([[2, 0]],[1,0]))
