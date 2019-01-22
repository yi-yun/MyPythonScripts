class Solution:        
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        list=[]
        for i in range(left, right+1):
            if (subself(self,i)):
                list.append(i)
        return list
def subself(self,n):
    a = str(n)
    num = 0
    for i in a:
        if int(i) == 0:
            continue
        if (n % int(i) == 0):
            num += 1
    if (num==len(a)):
        return True
    else:
        return False

def a(left, right):
    res = []
    for i in range(left, right + 1):
        d = i
        while (d):
            j = d % 10
            if not j:
                break
            if i % j:
                break
            d=d//10
        if not d:
            res.append(i)
    return res
print(a(1,22))