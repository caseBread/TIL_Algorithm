import sys
ip = sys.stdin.readline

n,m=map(int,ip().split())
arr = []
for _ in range(n) :
    arr.append(ip().strip("\n"))

dp=[[0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(1,n+1) :
    for j in range(1,m+1) :
        if arr[i-1][j-1] == "1" :
            dp[i][j] = min(dp[i-1][j-1],dp[i][j-1],dp[i-1][j])+1


res = 0
for i in dp :
    res = max(res,max(i))

print(res*res)