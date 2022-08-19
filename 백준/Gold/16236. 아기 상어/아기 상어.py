import sys
import heapq
from collections import deque
ip = sys.stdin.readline

direction = [[-1,0],[0,-1],[0,1],[1,0]]
INF = 1e9
n = int(ip())

arr = []

for j in range(n) :
    temp = list(map(int,ip().split()))
    for i in range(len(temp)) :
        if temp[i] == 9 :
            sy,sx = j,i
            temp[i] = 0
    arr.append(temp)

def bfs(y,x,arr,amount) :
    queue = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[y][x] = True
    queue.append([0,y,x])

    while queue :
        cnt,y,x = heapq.heappop(queue)
        if 0<arr[y][x]<amount : 
            return cnt,y,x
        for dy,dx in direction :
            ny,nx = dy+y,dx+x
            if 0<=ny<n and 0<=nx<n :
                if arr[ny][nx] <= amount and not visited[ny][nx] :
                    visited[ny][nx] = True
                    heapq.heappush(queue,[cnt+1,ny,nx])
                    
        
    return -1, -1, -1

amount = 2
distance = 0
eatCount = 0
while True :
    cnt,sy,sx = bfs(sy,sx,arr,amount)
    arr[sy][sx] = 0
    if cnt == -1 :
        print(distance)
        break
    
    distance += cnt
    eatCount += 1

    if eatCount == amount :
        amount += 1
        eatCount = 0


    