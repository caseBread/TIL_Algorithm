import sys
ip = sys.stdin.readline

n=int(ip())
arr = []
for _ in range(n) :
    arr.append(list(map(int,ip().split())))

arr2 = [[0 for _ in range(3)] for _ in range(2)]
now = 0
bef = 1
arr2[bef] = arr[0]
for i in range(1,n) :
    arr2[now][0] = arr[i][0] + max(arr2[bef][0],arr2[bef][1])
    arr2[now][1] = arr[i][1] + max(arr2[bef])
    arr2[now][2] = arr[i][2] + max(arr2[bef][1],arr2[bef][2])
    arr[i][0] = arr[i][0] + min(arr[i-1][0],arr[i-1][1])
    arr[i][1] = arr[i][1] + min(arr[i-1])
    arr[i][2] = arr[i][2] + min(arr[i-1][1],arr[i-1][2])
    temp = now
    now = bef
    bef = temp

print(max(arr2[bef]), min(arr[n-1]))
