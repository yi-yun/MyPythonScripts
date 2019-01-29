def find(target):
    length=len(target)
    res=[]
    for i in range(length):
        tmp=target[i]
        if i!=tmp:
            if tmp!=target[tmp]:
                target[i],target[target[i]]=target[target[i]],target[i]
            else:
                print(tmp)
                res.append(tmp)
    return res

print(find([2,3,1,0,2,5,3]))

