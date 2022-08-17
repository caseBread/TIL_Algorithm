import sys
from copy import deepcopy
from collections import deque
ip = sys.stdin.readline

direct = [[-1,0],[1,0],[0,-1],[0,1]]
arr = []
queue = deque()
n,k = map(int,ip().split())

for _ in range(n) :
    arr.append(list(map(int,ip().split())))
second = 0

for i in range(1,k+1) :
    for j in range(n) :
        for k in range(n) :
            if arr[j][k] == i :
                queue.append([j,k,arr[j][k],second])


s,X,Y = map(int,ip().split())

def bfs() :

    while queue :
        y,x,now,nowSecond = queue.popleft()
        if nowSecond == s :
            break
        for dy,dx in direct :
            ny,nx = dy+y,dx+x
            if 0 <= nx < n and 0 <= ny < n :
                if arr[ny][nx] == 0 :
                    arr[ny][nx] = now
                    queue.append([ny,nx,now,second+1])
        


    return arr[X-1][Y-1]
        
print(bfs())
