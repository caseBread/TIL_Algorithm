import sys
from collections import deque
ip = sys.stdin.readline

direction = deque([[0,1],[1,0],[0,-1],[-1,0]])

n = int(ip())
k = int(ip())

apple = [[False for _ in range(n+1)] for _ in range(n+1)]

for _ in range(k) :
    a,b = map(int,ip().split())
    apple[a][b] = True

L = int(ip())

navi = deque()

for _ in range(L) :
    a,b = ip().split()
    if b == 'D' :
        b = -1
    else :
        b = 1
    navi.append([int(a),b])

queue = deque()
queue.append([1,1])

cnt = 1
while queue :
    
    y,x = queue[-1]
    dy,dx = direction[0]

    if not (0 < y+dy <= n and 0 < x+dx <= n) :
        print(cnt)
        break
    elif [y+dy,x+dx] in queue :
        print(cnt)
        break

    queue.append([y+dy,x+dx])
    if not apple[y+dy][x+dx] :
        queue.popleft()
    else :
        apple[y+dy][x+dx] = False
    
    if len(navi) and cnt == navi[0][0] :
        direction.rotate(navi[0][1])
        navi.popleft()

    cnt += 1
