import sys
ip = sys.stdin.readline

n=int(ip())
dp = [1]*n

arr = list(map(int,ip().split()))

for i in range(1,n) :
    for j in range(i) :
        if arr[j] < arr[i] :
            dp[i] = max(dp[i],dp[j]+1)


print(max(dp))