import sys
ip = sys.stdin.readline

n,m = map(int,ip().split())

s = []
for _ in range(n) :
    s.append(ip())

s.sort()



def sol(t) :
    start = 0
    end = len(s)-1
    while start <= end :
        middle = (start+end)//2
        if s[middle] == t :
            return True
        elif s[middle] < t :
            start = middle + 1
        else :
            end = middle - 1
    
    return False

cnt = 0
for _ in range(m) :
    if sol(ip()) :
        cnt += 1

print(cnt)