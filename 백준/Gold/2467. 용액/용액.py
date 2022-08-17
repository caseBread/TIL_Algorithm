import sys
ip = sys.stdin.readline

n = int(ip())
arr = list(map(int,ip().split()))

rA = pA = 0
rB = pB = len(arr)-1
minn = 1e11

while pA < pB :
    if abs(arr[pA] + arr[pB]) < minn :
        rA = pA
        rB = pB
        minn = abs(arr[pA] + arr[pB])
    if arr[pA] + arr[pB] < 0 :
        pA+=1
    elif arr[pA] + arr[pB] > 0 :
        pB-=1
    else :
        rA = pA
        rB = pB
        break

    
print(arr[rA],arr[rB])