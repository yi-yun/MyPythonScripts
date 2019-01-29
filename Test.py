def test(target):
    i=target[0]
    i,target[i]=target[i],i
    return target

print(test([2,0,1]))