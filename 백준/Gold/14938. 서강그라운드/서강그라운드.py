import sys
ip = sys.stdin.readline
INF = 1e9
n,m,r = map(int,ip().split())
item = list(map(int,ip().split()))

visited = [False] * (n+1)
distance = [INF] * (n+1)
graph = [[INF for _ in range(n+1)] for _ in range(n+1)]

for _ in range(r) :
    a,b,l = map(int,ip().split())
    graph[a][b] = l
    graph[b][a] = l
for i in range(1,n+1) :
    graph[i][i] = 0
for k in range(1,n+1) :
    for i in range(1,n+1) :
        for j in range(1,n+1) :
            graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])

cnt = [0]*(n+1)
for i in range(1,n+1) :
    for j in range(1,n+1) :
        if graph[i][j] <= m :
            cnt[i] += item[j-1]

print(max(cnt))



