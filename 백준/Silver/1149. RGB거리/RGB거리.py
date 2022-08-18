import sys
ip = sys.stdin.readline

n=int(ip())
arr=[]
for _ in range(n) :
    x,y,z=map(int,ip().split())
    arr.append([x,y,z])
dp=[[0 for _ in range(3)] for _ in range(n)]
dp[0] = arr[0]
for i in range(1,n) :
    dp[i][0] = arr[i][0] + min(dp[i-1][1],dp[i-1][2])
    dp[i][1] = arr[i][1] + min(dp[i-1][0],dp[i-1][2])
    dp[i][2] = arr[i][2] + min(dp[i-1][0],dp[i-1][1])

print(min(dp[n-1]))