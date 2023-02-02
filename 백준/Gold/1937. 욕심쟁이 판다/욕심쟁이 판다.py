import sys
ip = sys.stdin.readline
sys.setrecursionlimit(10**5)

direct = [[-1,0],[1,0],[0,-1],[0,1]]
n=int(ip())
arr=[]
dp = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(n) :
    t = list(map(int,ip().split()))
    arr.append(t)


def dfs(y,x) :
    ok = True

    for dy,dx in direct :
        if 0 <= y+dy < n and 0 <= x+dx < n :
            if arr[y][x] < arr[y+dy][x+dx] :
                ok = False
                if dp[y+dy][x+dx] == 0 :
                    dp[y][x] = max(dp[y][x],dfs(y+dy,x+dx))
                else :
                    dp[y][x] = max(dp[y][x],dp[y+dy][x+dx]+1)
    if ok :
        dp[y][x] = 1


    return dp[y][x]+1

def sol(start) :
    for a in start :
        dfs(a[0],a[1])
        
def check(i,j) :
    for dy,dx in direct :
        if 0 <= i+dy<n and 0<=j+dx<n :
            if arr[i+dy][j+dx] < arr[i][j] :
                return False    

    return True

start=[]
for i in range(n) :
    for j in range(n) :
        if check(i,j) :
            start.append([i,j])

sol(start)

maxx = 0
for i in dp :
    maxx = max(maxx,max(i))
print(maxx)