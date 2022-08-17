import sys
from collections import deque
ip = sys.stdin.readline
INF = 1e9
t = int(ip())

# def dfs(time, graph, cost, now) :
#     if not graph[now] :
#         return time,graph, cost
#     for i in graph[now] :
#         if cost[i] < cost[now]+time[i] :
#             cost[i] = cost[now]+time[i]
#             time,graph, cost = dfs(time,graph, cost, i)

#     return time,graph, cost

# def recursive(graph, time, now) :
#     if not graph[now] :
#         return time[now]
#     maxx = 0
#     for i in graph[now] :
#         maxx = max(maxx,recursive(graph,time,i) + time[now])
#     return maxx

def dp(time,cost,graph,start) :
    queue = deque()
    queue.append(start)
    cost[start] = time[start]
    while queue :
        now = queue.popleft()
        for i in graph[now] :
            if (cost[i] < cost[now]+time[i]) :
                cost[i] = cost[now]+time[i]
                queue.append(i)
    
    return cost



for _ in range(t) :
    n,k = map(int,ip().split())
    time = [0] + list(map(int,ip().split()))
    graph = [[] for _ in range(n+1)]
    isStart = [False] * (n+1)
    for _ in range(k) :
        x,y = map(int,ip().split())
        graph[x].append(y)
        isStart[y] = True
    
    cost = [0]*(n+1)
    w = int(ip())

    for i in range(len(isStart)) :
        if not isStart[i] :
            cost = dp(time,cost,graph,i)
    # result = recursive(graph, time, w)
    print(cost[w])
    