import sys
ip = sys.stdin.readline
from collections import deque

direct = [[-1,0],[1,0],[0,-1],[0,1]]

n,m = map(int,ip().split())
arr=[]

for _ in range(n) :
    arr.append(ip().strip("\n"))

def bfs(i,j) :
    maxx = 0
    queue=deque()
    visited=[[False for _ in range(m)] for _ in range(n)]
    queue.append([i,j,0])
    visited[i][j] = True
    while queue :
        y,x,cnt = queue.popleft()
        maxx = max(maxx,cnt)
        for dy,dx in direct :
            if 0 <= y+dy < n and 0 <= x+dx < m :
                if arr[y+dy][x+dx] == "L" and not visited[y+dy][x+dx] :
                    visited[y+dy][x+dx] = True
                    queue.append([y+dy,x+dx,cnt+1])

    return maxx

def isPossible(y,x) :
    ok = True

    if arr[y][x] == "W" :
        return False
    for dy,dx in direct :
        if 0 <= y+dy < n and 0 <= x+dx < m :
            if arr[y+dy][x+dx] == "L" :
                if 0 <= y-dy < n and 0 <= x-dx < m :
                    if arr[y-dy][x-dx] == "L" :
                        ok = False

    return ok


maxx = 0
for i in range(n) :
    for j in range(m) :
        if isPossible(i,j):
            maxx = max(maxx,bfs(i,j))

print(maxx)