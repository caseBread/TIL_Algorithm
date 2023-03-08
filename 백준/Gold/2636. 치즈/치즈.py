import sys
ip = sys.stdin.readline
from collections import deque
n,m = map(int,ip().split())
direction = [[-1,0],[1,0],[0,-1],[0,1]]

cheeze = []

cheeze_cnt = 0
for _ in range(n) :
  temp = list(map(int,ip().split()))
  cheeze_cnt += temp.count(1)
  cheeze.append(temp)



def bfs(start) :
  queue = deque()
  side = []
  queue.append(start)
  visited = [[False for _ in range(m)] for _ in range(n)]
  visited[start[0]][start[1]] = True
  while queue :
    y,x = queue.popleft()
    for dy,dx in direction :
      if 0 <= y+dy < n and 0 <= x+dx < m :
        if not visited[y+dy][x+dx] :
          visited[y+dy][x+dx] = True
          if cheeze[y+dy][x+dx] == 1 :
            side.append([y+dy,x+dx])
          else :
            queue.append([y+dy,x+dx])
          
  return side

def cheeze_remove(remove_list) :
  for y,x in remove_list :
    cheeze[y][x] = 0

cnt = 0
last_cnt = cheeze_cnt
while cheeze_cnt :
  remove_list = bfs([0,0])
  cheeze_remove(remove_list)
  cheeze_cnt -= len(remove_list)
  if cheeze_cnt != 0 :
    last_cnt = cheeze_cnt
  cnt += 1


print(cnt)
print(last_cnt)