#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re

#请完成下面这个函数，实现题目要求的功能
#当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^ 
#******************************开始写代码******************************


def  string2int(str):
    try:
        float(str)
    except:
        return 0
    cnt=0
    for i in str:
        if i is ".":
            cnt+=1
    if cnt==1:
        return str.split(".")[0]
    elif cnt>1:
        return 0
    else:
        try:
            a=int(str)
        except:
            a=0
        return a
    # cnt=0
    # for i in str:
    #     if i !=".":
    #         try:
    #             a=int (i)
    #         except:
    #             return 0
    #     else:
    #         cnt+=1
    # if cnt==0:
    #     return int(str)
    # elif cnt==1:
    #     return str.split(".")[0]
    # else:
    #     return 0



#******************************结束写代码******************************

if __name__ == "__main__":
    
    try:
        _str = input()
    except:
        _str = None
    
    if _str[0]=='-':
        res = string2int(_str[1:])
    else:
        res = string2int(_str)

    print(str(res) + "\n")