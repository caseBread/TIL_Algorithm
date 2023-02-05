import sys
ip = sys.stdin.readline

arr=[]
summ = 0
minn = 1e9
for _ in range(7) :
    x = int(ip())
    if x % 2 == 1 :
        summ += x
        minn = min(minn,x)

if (summ != 0) :
    print(summ)
    print(minn)
else :
    print(-1)

