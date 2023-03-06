import sys
ip = sys.stdin.readline
INF=int(1e9)
n=int(ip())
dp = [[0] * (1 << n) for _ in range(n)]
graph = []
for _ in range(n) :
  graph.append(list(map(int,ip().split())))

def dfs(now,visited): 
  global dp
  if visited == (1 << n) - 1 : # 비트마스크가 11111... 인 경우 (모든 노드를 거친 경우) => 처음으로 돌아가야함
    if graph[now][0] > 0 : # 처음으로 돌아가는 길이 있는지?
      return graph[now][0]
    else :
      return INF
  
  if dp[now][visited] != 0 : # memo된 값이 있다면
    return dp[now][visited]

  dp[now][visited] = INF

  for i in range(1,n) : # visited를 처음을 제외한 모든 노드 조사 (처음은 맨 마지막에 돌아가야함, 앞에서 조건문 걸어줌.)
    if graph[now][i] == 0 : # 갈 수 있는 길이 없다면 스킵
      continue
    if visited & (1 << i) : # 이미 가본 도시면 스킵 (visited의 비트마스킹에서 i번째 비트가 1인지 검사)
      continue

    # now번째도시에서의 이동 = i번째도시에서의 이동 + now에서 i로 이동 비용 
    # now번째 도시에서의 이동의 최솟값 찾아야함
    dp[now][visited] = min(dp[now][visited], dfs(i,visited | (1 << i)) + graph[now][i]) 
  
  return dp[now][visited]

result = dfs(0,1)

print(result)