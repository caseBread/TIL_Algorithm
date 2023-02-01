import sys
ip = sys.stdin.readline

res = ""
a = ip().strip("\n")
b = ip().strip("\n")

dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]

for i in range(len(a)) :
    for j in range(len(b)) :
        if a[i] == b[j] :
            dp[i+1][j+1] = dp[i][j]+1
        else :
            dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j])



def getStr(i,j) :
    global res

    if dp[i][j] == dp[i][j-1] :
        getStr(i,j-1)
    elif dp[i][j] == dp[i-1][j] :
        getStr(i-1,j)
    else :
        res += a[i-1]
        if dp[i][j] == 1 :
            return
        getStr(i-1,j-1)


print(dp[len(a)][len(b)])
if dp[len(a)][len(b)] != 0 :
    getStr(len(a),len(b))
    print(res[::-1])

