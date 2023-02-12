import sys
ip = sys.stdin.readline
from collections import deque

s=ip().strip("\n")

res = []

temp = ""
tag = False
for i in s :
    if i == "<" :
        tag = True
        res.append(temp[::-1])
        temp = "<"

    elif i == ">" :
        res.append(temp + ">")
        temp = ""
        tag = False
    elif not tag :
        if i != " " :
            temp += i
        else :
            res.append(temp[::-1]+" ")
            temp = ""
    else :
        temp += i

if temp :
    res.append(temp[::-1])
for i in res :
    if i :
        print(i,end="")
