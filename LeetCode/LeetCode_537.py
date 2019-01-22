class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        list1=a.split('+')
        reala=int(list1[0])
        xua = int(list1[1][:-1])

        list2=b.split('+')
        realb = int(list2[0])
        xub = int(list2[1][:-1])
        # print(type(realb))
        
        return str(reala * realb - xua * xub)+'+'+str(reala * xub + realb * xua)+'i'
        
print(Solution().complexNumberMultiply("78+-76i","-86+72i"))