from collections import deque
res = 1000000000
arr = []
def dfs(noA,now,summ) :
    global res
    right = 0
    left = 0
    if not noA :
        res = min(res,summ)
        return
    if len(noA) > 1 :
        if now == 0 :
            right = noA[1]-noA[0]
            left = len(arr) - (noA[-1]-noA[0])
        else :
            right = len(arr) - (noA[-1]-noA[0])
            left = noA[-1]-noA[-2]
    t = noA[now]
    del noA[now]
    dfs(noA,0,summ+right)
    dfs(noA,-1,summ+left)
    if now == 0 :
        noA.appendleft(t)
    else :
        noA.append(t)
    

def solution(name):
    
    arr.append(ord(name[0])-65)
    noA = deque([0])
    noAA = [0]
    for i in range(1,len(name)) :
        arr.append(ord(name[i])-65)
        if ord(name[i])-65 != 0 :
            noA.append(i)

           
    dfs(noA,0,0)

    basic = 0
    for i in noA :
        basic += min(arr[i],(26-arr[i]))


    return res+basic